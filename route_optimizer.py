import math
from route_data import Route

def calculate_distance(loc1, loc2):
    """Calculate Euclidean distance between two locations"""
    x_diff = loc1.latitude - loc2.latitude
    y_diff = loc1.longitude - loc2.longitude
    return math.sqrt(x_diff**2 + y_diff**2) * 100  # Rough km conversion

def estimate_route_duration(route):
    """Estimate how long a route will take in minutes"""
    if not route.deliveries or not route.depot:
        return 0
    
    total_distance = 0
    current_loc = route.depot
    
    # Calculate distance from depot to first delivery
    if route.deliveries:
        total_distance += calculate_distance(current_loc, route.deliveries[0].location)
        current_loc = route.deliveries[0].location
    
    # Add distances between deliveries
    for i in range(1, len(route.deliveries)):
        delivery = route.deliveries[i]
        total_distance += calculate_distance(current_loc, delivery.location)
        current_loc = delivery.location
    
    # Add return to depot
    total_distance += calculate_distance(current_loc, route.depot)
    
    # Calculate time based on vehicle speed (km/h → minutes)
    return (total_distance / route.vehicle.speed) * 60

class RouteOptimizer:
    def __init__(self, routes, vehicles, depot):
        self.routes = routes
        self.vehicles = vehicles
        self.depot = depot
        self.next_route_id = max([r.id for r in routes]) + 1 if routes else 1
    
    def handle_route_incident(self, incident):
        """Reallocate deliveries when a route has an incident"""
        # Find the affected route
        affected_route = None
        for route in self.routes:
            if route.id == incident.route_id:
                affected_route = route
                break
        
        if not affected_route:
            return False
        
        # Mark the route as inactive
        affected_route.active = False
        
        # If it's a vehicle breakdown, mark vehicle as unavailable
        if incident.type.name == "VEHICLE_BREAKDOWN":
            affected_route.vehicle.available = False
        
        # Get undelivered deliveries from the affected route
        pending_deliveries = [d for d in affected_route.deliveries if not d.completed]
        
        # Reallocate deliveries to other routes or create new ones
        self._reallocate_deliveries(pending_deliveries)
        
        return True
    
    def _reallocate_deliveries(self, deliveries):
        """Reallocate deliveries to existing routes or create new ones"""
        # Sort deliveries by priority (highest first)
        sorted_deliveries = sorted(deliveries, key=lambda d: d.priority, reverse=True)
        
        # Available routes
        available_routes = [r for r in self.routes if r.active]
        
        # Available vehicles not currently on routes
        used_vehicle_ids = [r.vehicle.id for r in available_routes]
        available_vehicles = [v for v in self.vehicles if v.available and v.id not in used_vehicle_ids]
        
        # Try to fit deliveries into existing routes
        remaining_deliveries = []
        for delivery in sorted_deliveries:
            assigned = False
            
            # Try to add to existing routes
            for route in available_routes:
                # Check if adding this delivery would still allow completion within time windows
                route.add_delivery(delivery)
                new_duration = estimate_route_duration(route)
                
                # Simple check: if new duration is acceptable (less than 8 hours)
                if new_duration < 480:  # 8 hours in minutes
                    assigned = True
                    break
                else:
                    # Remove if not feasible
                    route.remove_delivery(delivery.id)
            
            if not assigned:
                remaining_deliveries.append(delivery)
        
        # Create new routes for remaining deliveries if vehicles are available
        while remaining_deliveries and available_vehicles:
            new_vehicle = available_vehicles.pop(0)
            new_route = Route(self.next_route_id, new_vehicle, [], self.depot)
            self.next_route_id += 1
            
            # Add as many deliveries as possible to the new route
            i = 0
            while i < len(remaining_deliveries):
                delivery = remaining_deliveries[i]
                new_route.add_delivery(delivery)
                
                # Check if route is still feasible
                new_duration = estimate_route_duration(new_route)
                if new_duration < 480:  # 8 hours
                    remaining_deliveries.pop(i)
                else:
                    # Remove if not feasible
                    new_route.remove_delivery(delivery.id)
                    i += 1
            
            # Add the new route
            self.routes.append(new_route)
            
        return remaining_deliveries  # These couldn't be assigned
    
    def print_route_summary(self):
        """Print a summary of all routes"""
        print("\n===== ROUTE SUMMARY =====")
        for route in self.routes:
            if route.active:
                print(f"\nRoute {route.id} - Vehicle: {route.vehicle.name}")
                print(f"Estimated Duration: {estimate_route_duration(route):.1f} minutes")
                print("Deliveries:")
                for d in route.deliveries:
                    print(f"  - {d}")