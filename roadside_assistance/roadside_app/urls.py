# roadside_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view
from . import views  # Import your views here
from .views import reg_view, reg2_view
from .views import service_provider_list
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path
from django.urls import path
from .views import view_requests, get_booking_details

# from .views import towtruck_view, workshop_view, ambulance_view, petrolbunk_view
# from .views import create_towing_service, create_petrol_bunk_service, create_workshop_service, create_ambulance_service


from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.reg_view, name='register'),

    path('register/', reg_view, name='register'),
    path('register/service/<int:user_id>/', reg2_view, name='reg2'),  # Route for service provider registration
    

    # User Dashboard URL
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'), 
    path('user_update_profile/', views.user_update_profile, name='user_update_profile'),
    path('request-assistance/', views.request_assistance, name='request_assistance'),

    #request
    path('towtruck-request/', views.tow_truck_request, name='towtruck_request'),
    path('petrolbunk-request/', views.petrol_bunk_request, name='petrolbunk_request'),
    path('ambulance-request/', views.ambulance_request, name='ambulance_request'),
    path('workshop-request/', views.workshop_request, name='workshop_request'),

    #book
    path('book/<int:provider_id>/', views.book_service, name='book_service'),

    #history
    path('service-history/', views.service_history, name='service_history'),

   
    # path('towtruck/', towtruck_view, name='towtruck'),
    # path('workshop/', workshop_view, name='workshop'),
    # path('ambulance/', ambulance_view, name='ambulance'),
    # path('petrolbunk/', petrolbunk_view, name='petrolbunk'),



    # path('towing-service/', create_towing_service, name='create_towing_service'),
    # path('petrol-bunk-service/', create_petrol_bunk_service, name='create_petrol_bunk_service'),
    # path('workshop-service/', create_workshop_service, name='create_workshop_service'),
    # path('ambulance-service/', create_ambulance_service, name='create_ambulance_service'),


    #serviceprovider Dashboard URL
    path('serviceprovider_dashboard/', views.service_provider_dashboard, name='service_provider_dashboard'),
    path('update-profile/', views.update_profile, name='update_profile_service_provider'),

    path('service-provider/view_requests/', views.view_requests, name='view_requests'),
    path('view-requests/', views.view_requests, name='view_requests'),
    path('approve-booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),

    path('service-history/', views.service_history1, name='service_history1'),
   
    

    #Password
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Admin Dashboard URL
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view-users/', views.view_users, name='view_users'),
    path('toggle_active_status/<int:user_id>/', views.toggle_active_status, name='toggle_active_status'),
    path('admin-profile-update/', views.admin_profile_update,name='admin_profile_update'),
    path('service-providers/', views.service_provider_list, name='service_provider_list'),

  


]





