# roadside_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import login_view

from . import views  # Import your views here
from django.urls import path
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)



urlpatterns = [



    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.reg_view, name='register'),
 
 
    path('login/', login_view, name='login'),
    


    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),  # User Dashboard URL
    path('update_profile/', views.update_profile, name='update_profile'),



    path('service-provider-dashboard/', views.service_provider_dashboard, name='service_provider_dashboard'),  # Service Provider Dashboard URL

 # Admin Dashboard URL
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/view-users/', views.view_users, name='view_users'),

    #.................................#
    #password
       # urls.py
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),


    


    # path('view-users/', views.view_users, name='view_users'),
    # path('view-service-providers/', views.view_service_providers, name='view_service_providers'),
    # path('add-service-types/', views.add_service_types, name='add_service_types'),
    # path('order-items/', views.order_items, name='order_items'),
    # path('view-feedback/', views.view_feedback, name='view_feedback'),
    # path('view-incident-report/', views.view_incident_report, name='view_incident_report'),
    # path('manage-orders/', views.manage_orders, name='manage_orders'),
    # path('manage-product-details/', views.manage_product_details, name='manage_product_details'),
    # path('home/', views.home, name='home'),  # Log out link directs here 
]



  


