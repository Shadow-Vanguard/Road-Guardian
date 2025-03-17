# utils.py

from django.core.mail import send_mail
from django.conf import settings
import requests
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def send_activation_email(user, action):
    subject = f'Your account has been {action}'
    
    if action == 'activated':
        message = f'Hello {user.name},\n\nYour account has been {action} by the admin.\n\nThank you!'
    elif action == 'deactivated':
        message = f'Hello {user.name},\n\nYour account has been {action} by the admin. If you want to know more please contact the admin.\n\n If you need to contact email as in road.guardian08@gmail.com.\n\n Thank you!'
    else:
        message = f'Hello {user.name},\n\nYour account status has been updated.\n\nThank you!'

    recipient_list = [user.email]

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

def calculate_optimized_route(user_location, service_provider_location, incidents):
    """
    Calculate the optimized route from user_location to service_provider_location using OpenStreetMap data.
    
    Parameters:
    - user_location: str, the user's location in "latitude,longitude" format
    - service_provider_location: str, the service provider's location in "latitude,longitude" format
    - incidents: list, a list of incidents that may affect the route (not used in this example)

    Returns:
    - optimized_route: list, a list of nodes representing the optimized route
    """
    # Split the locations into latitude and longitude
    user_lat, user_lon = map(float, user_location.split(","))
    provider_lat, provider_lon = map(float, service_provider_location.split(","))

    # Create a graph from the OSM data
    G = ox.graph_from_point((user_lat, user_lon), dist=1000, network_type='drive')

    # Get the nearest nodes to the user and service provider locations
    user_node = ox.distance.nearest_nodes(G, user_lon, user_lat)
    provider_node = ox.distance.nearest_nodes(G, provider_lon, provider_lat)

    # Calculate the shortest path
    optimized_route = nx.shortest_path(G, user_node, provider_node, weight='length')

    # Return the optimized route as a list of node IDs
    return optimized_route

def plot_route(G, route):
    """
    Plot the optimized route on the graph.
    
    Parameters:
    - G: The graph from OSM data.
    - route: The list of nodes representing the optimized route.
    """
    # Plot the graph and the route
    fig, ax = ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, bgcolor='k')
    plt.show()