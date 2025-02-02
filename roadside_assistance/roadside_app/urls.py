# roadside_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view
from . import views  # Import your views here
from .views import reg_view, reg2_view
from .views import service_provider_list
from django.contrib.auth import views as auth_views
from django.urls import path, include
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
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.reg_view, name='register'),

    path('oauth/', include('social_django.urls', namespace='social')),

    path('register/', reg_view, name='register'),
    path('register/service/<int:user_id>/', views.reg2_view, name='reg2'),


    # User Dashboard URL
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'), 
    # path('user_update_profile/', views.user_update_profile, name='user_update_profile'),
    path('profile/view/', views.user_profile_view, name='user_profile_view'),  # URL for viewing profile
    path('profile/edit/', views.user_profile_edit, name='user_profile_edit'),  # URL for editing profile

    path('request-assistance/', views.request_assistance, name='request_assistance'),#request assistance
    path('service-providers/<int:service_type_id>/', views.service_providers_list, name='service_providers_list'),#service providers list
    path('book-assistance/<int:provider_id>/', views.book_assistance, name='book_assistance'),#book assistance
    path('get-category-charge/', views.get_category_charge, name='get_category_charge'),#get category charge

    path('user-service-history/', views.user_service_history, name='user_service_history'),#user service history
    path('report-incident/', views.report_incident, name='report_incident'),#report incident

    path('payment-history/', views.payment_history, name='payment_history'),#payment history
    path('pay-bill/<int:bill_id>/', views.pay_bill_view, name='pay_bill'),  # New URL for paying a bill
    
    path('pay-bill/<int:bill_id>/', views.pay_bill_view, name='pay_bill'),  # New URL for paying a bill
    path('payment-success/<int:bill_id>/', views.payment_success_view, name='payment_success'),  # New URL for payment success


    #serviceprovider Dashboard URL
    path('service-provider/dashboard/', views.service_provider_dashboard, name='service_provider_dashboard'),
    path('update-profile/', views.update_profile, name='update_profile_service_provider'),
    
    path('service-provider/service-history/', views.view_service_history, name='view_service_history'),#view service history
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),#submit feedback
    path('get-bookings/', views.get_bookings, name='get_bookings'),#get bookings
    path('service-provider/view-feedback/', views.view_feedback, name='view_feedback'),#view feedback
    path('payments/', views.view_payments, name='view_payment'),  # view payments


    path('view_requests/', views.view_requests, name='view_requests'),
    path('accept_booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('start_service/<int:booking_id>/', views.start_service, name='start_service'),
    path('complete_service/<int:booking_id>/', views.complete_service, name='complete_service'),

    path('bill/<int:booking_id>/', views.bill_view, name='bill_view'),
    path('submit_bill/<int:booking_id>/', views.submit_bill, name='submit_bill'),
    path('get_bill_details/<int:booking_id>/', views.get_bill_details, name='get_bill_details'),


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


    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),






    ########################################################################################################################

    path('api/chatbot/', views.chatbot_response, name='chatbot_response'),
  


    path('bill/', views.bill_view, name='bill_view'),
    path('submit-bill/', views.submit_bill, name='submit_bill'),
    path('send-payment-request/', views.send_payment_request, name='send_payment_request'),

    path('process-image/', views.process_image, name='process_image'),

    path('api/chatbot/', views.chatbot_response, name='chatbot_response'),





    




]





