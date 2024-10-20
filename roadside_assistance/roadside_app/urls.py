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
    path('register/service/<int:user_id>/', views.reg2_view, name='reg2'),


    # User Dashboard URL
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'), 
    path('user_update_profile/', views.user_update_profile, name='user_update_profile'),

    path('request-assistance/', views.request_assistance, name='request_assistance'),
    path('service-providers/<int:service_type_id>/', views.service_providers_list, name='service_providers_list'),
    path('book-assistance/<int:provider_id>/', views.book_assistance, name='book_assistance'),
    path('get-category-charge/', views.get_category_charge, name='get_category_charge'),


    #serviceprovider Dashboard URL
    path('serviceprovider_dashboard/', views.service_provider_dashboard, name='service_provider_dashboard'),
    path('update-profile/', views.update_profile, name='update_profile_service_provider'),

    

    #Password
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Admin Dashboard URL
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view-users/', views.view_users, name='view_users'),#view users
    path('toggle_active_status/<int:user_id>/', views.toggle_active_status, name='toggle_active_status'),
    path('admin-profile-update/', views.admin_profile_update,name='admin_profile_update'),#admin profile update
    path('service-providers/', views.service_provider_list, name='service_provider_list'),#service provider list

    #add edit delete service type
    path('manage-service-types/', views.manage_service_types, name='manage_service_types'),
    path('edit-service-type/<int:servicetype_id>/', views.edit_service_type, name='edit_service_type'),
    path('delete-service-type/<int:servicetype_id>/', views.delete_service_type, name='delete_service_type'),

    #add edit delete service category
    path('manage-service-categories/', views.manage_service_categories, name='manage_service_categories'),
    path('edit-service-category/<int:category_id>/', views.edit_service_category, name='edit_service_category'),
    path('delete-service-category/<int:category_id>/', views.delete_service_category, name='delete_service_category'),

  


]





