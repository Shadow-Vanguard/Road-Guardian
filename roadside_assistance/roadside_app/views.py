from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm, ServiceProviderForm
from .models import ServiceProvider


  
#login
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser  # Assuming you have a CustomUser model

from django.contrib.auth import get_user_model

User = get_user_model()

def is_user_active(username):
    try:
        user = User.objects.get(username=username)
        return user.is_active  # Return True if active, False if not
    except User.DoesNotExist:
        return False  # User does not exist

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.utils.cache import add_never_cache_headers

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_active:  # Check if the user is active
                    messages.error(request, "Your account has been deactivated. Please contact admin.")
                    return render(request, 'login.html', {'form': form})  # Return the form with the message
                else:
                    # Log the user in and create session
                    auth_login(request, user)
                   

                    # Redirect based on the user role
                    if user.is_superuser:
                        request.session['admin_id'] = user.id  # Store the user ID in session
                        return redirect('admin_dashboard')
                    
                    elif user.role == 'user':
                        request.session['user_id'] = user.id  # Store the user ID in session
                        return redirect('user_dashboard')
                    
                    elif user.role == 'service_provider':
                        request.session['service_provider_id'] = user.id  # Store the user ID in session
                        return redirect('service_provider_dashboard')
                    else:
                        return redirect('home')  # Default redirection
            else:
                # Authentication failed, show appropriate message
                try:
                    user = CustomUser.objects.get(username=username)
                    if not user.is_active:
                        messages.error(request, "Your account has been deactivated. Please contact admin.")
                    else: 
                        messages.error(request, 'Invalid username or password.')
                except CustomUser.DoesNotExist:
                    messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



#Registration
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegistrationForm, ServiceProviderForm
from .models import CustomUser, ServiceProvider

from django.shortcuts import render, redirect
from .models import ServiceProvider, ServiceType  # assuming these are your models
from .forms import ServiceProviderForm

def reg_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save user before any further actions
            
            if user.role == 'service_provider':
                return redirect('reg2', user_id=user.id)  # Redirect to the service provider registration form
            else:
                messages.success(request, 'Registration successful!')
                return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Registration failed. Please check the details and try again.')
    else:
        form = RegistrationForm()
    
    return render(request, 'reg.html', {'form': form})

from django.http import HttpResponseRedirect
from django.urls import reverse

def reg2_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)  # Get the user or 404
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            service_provider = form.save(commit=False)
            service_provider.user = user  # Link to the service provider's user account
            service_provider.save()
            messages.success(request, 'Service provider registration successful!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceProviderForm()
    
    return render(request, 'reg2.html', {'form': form}) 




def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib import messages

def logout_view(request):
    auth_logout(request)  # Log the user out
    request.session.flush()  # Clear all session data
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to the login page



#password reset

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm

class CustomPasswordResetView(auth_views.PasswordResetView):
    """
    Handles the display and processing of the password reset form.
    """
    template_name = 'password/password_reset.html'
    email_template_name = 'password/password_reset_email.html'
    subject_template_name = 'password/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    form_class = CustomPasswordResetForm

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    Informs the user that an email has been sent for password reset.
    """
    template_name = 'password/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    Handles the setting of a new password.
    """
    template_name = 'password/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = CustomSetPasswordForm

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """
    Informs the user that the password has been successfully reset.
    """
    template_name = 'password/password_reset_complete.html'

########################################################################################################


# User View

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm

from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import CustomUser, ServiceType, Incident
from .forms import CustomUserUpdateForm

@never_cache
@login_required
def user_dashboard(request):
    # Check if the user exists in the CustomUser model
    if 'user_id' in request.session:
        try:
            custom_user = CustomUser.objects.get(username=request.user.username)
        except CustomUser.DoesNotExist:
            # Create a new CustomUser if it doesn't exist
            custom_user = CustomUser.objects.create(
                username=request.user.username,
                email=request.user.email,
                name=request.user.get_full_name() or request.user.username,
                role='user'
            )

        # Handle form submission for user updates
        if request.method == 'POST':
            form = CustomUserUpdateForm(request.POST, instance=custom_user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your changes have been saved.')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CustomUserUpdateForm(instance=custom_user)

        # Fetch service types
        service_types = ServiceType.objects.all()

        # Fetch reported incidents for the logged-in user
        incidents = Incident.objects.filter()

        # Combine all context data
        context = {
            'form': form,
            'user': custom_user,
            'service_types': service_types,
            'incidents': incidents,
        }
        
        return render(request, 'user/user_dashboard.html', context)
    else:
        return redirect('login')

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def user_profile_view(request):
    return render(request, 'user/user_profile_view.html', {'user': request.user})

    
#update_profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserUpdateForm  # Ensure you have this form defined
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def user_profile_edit(request):
    user = request.user  # Get the current logged-in user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)  # Bind the form with the POST data
        if form.is_valid():
            form.save()  # Save the updated user information
            messages.success(request, 'Your profile has been updated.')  # Success message
            # Redirect based on user role
            if user.role == 'service_provider':
                return redirect('service_provider_dashboard')  # Updated to match URL pattern name
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')  # Error message
    else:
        form = CustomUserUpdateForm(instance=user)  # Load the current user data into the form

    return render(request, 'user/user_profile_edit.html', {'form': form})  # Render the edit profile template


# Request_Assistance

from django.shortcuts import render
from .models import ServiceType, ServiceProvider
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def request_assistance(request):
    # Fetch all service types
    service_types = ServiceType.objects.all()

    # Fetch all service providers
    service_providers = ServiceProvider.objects.select_related('user', 'service_type').all()

    context = {
        'service_types': service_types,
        'service_providers': service_providers,
    }
    return render(request, 'user/request_assistance.html', context)


from django.shortcuts import render
from .models import ServiceType
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def request_assistance(request):
    service_types = ServiceType.objects.all()
    return render(request, 'user/request_assistance.html', {'service_types': service_types})

#showing service_providers_list
from django.shortcuts import render, get_object_or_404
from .models import ServiceType, ServiceProvider
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def service_providers_list(request, service_type_id):
    service_type = get_object_or_404(ServiceType, servicetype_id=service_type_id)
    service_providers = ServiceProvider.objects.filter(service_type=service_type)
    return render(request, 'user/service_providers_list.html', {
        'service_type': service_type,
        'service_providers': service_providers
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceProvider, ServiceTypeCategory
from .forms import BookAssistanceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def book_assistance(request, provider_id):
    service_provider = get_object_or_404(ServiceProvider, pk=provider_id)
    
    if request.method == 'POST':
        form = BookAssistanceForm(request.POST, service_provider=service_provider)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service_provider = service_provider
            booking.save()
            messages.success(request, 'Assistance booked successfully!')
            # Redirect to the service providers list for the same service type
            return redirect('service_providers_list', service_type_id=service_provider.service_type.servicetype_id)
    else:
        form = BookAssistanceForm(service_provider=service_provider)
    
    context = {
        'form': form,
        'service_provider': service_provider,
    }
    return render(request, 'user/book_assistance.html', context)

    
from django.http import JsonResponse
from .models import ServiceTypeCategory
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def get_category_charge(request):
    category_id = request.GET.get('category_id')
    try:
        category = ServiceTypeCategory.objects.get(pk=category_id)
        return JsonResponse({'charge': category.charge})
    except ServiceTypeCategory.DoesNotExist:
        return JsonResponse({'charge': ''}, status=404)
        
        
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback, ServiceProvider, Booking
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, user=request.user)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "Thank you! Your feedback has been submitted successfully.")
            return redirect('user_dashboard')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = FeedbackForm(user=request.user)
    
    return render(request, 'user/feedback.html', {'form': form})



@never_cache
@login_required
def get_bookings(request):
    service_provider_id = request.GET.get('service_provider_id')
    bookings = Booking.objects.filter(
        user=request.user,
        service_provider_id=service_provider_id,
        status='completed'
    ).values('id', 'created_at', 'service_type_category__category_name')
    return JsonResponse(list(bookings), safe=False)



@never_cache
@login_required
def user_service_history(request):
    # Fetch user's service history with related service provider and service type category
    service_history = Booking.objects.filter(
        user=request.user
    ).select_related('service_provider', 'service_type_category').order_by('-created_at')
    
    # Fetch bills related to the user's bookings
    bills = Bill.objects.filter(user=request.user.username)  # Adjust if necessary based on your user model

    context = {
        'service_history': service_history,
        'bills': bills,  # Add bills to the context
        'user': request.user,
    }
    return render(request, 'user/user_service_history.html', context)

from django.shortcuts import render
from .models import Bill
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def payment_history(request):
    # Fetch the bills for the logged-in user
    bills = Bill.objects.filter(user=request.user.name)  # Adjust as necessary
    return render(request, 'user/payment_history.html', {'bills': bills})

# Add this import at the top of your views.py file
from django.shortcuts import get_object_or_404, redirect
from .models import Bill
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def pay_bill_view(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, user=request.user.name)  # Ensure the bill belongs to the current user
    bill.status = 'paid'  # Update the status to 'paid'
    bill.save()  # Save the changes
    return redirect('payment_history')  # Redirect back to the payment history page



# Add these imports at the top of your views.py file
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_SECRET_KEY))


@never_cache
@login_required
def pay_bill_view(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id, user=request.user.name)  # Ensure the bill belongs to the current user

    if request.method == 'POST':
        # Create a Razorpay order
        order_amount = int(bill.total_amount * 100)  # Amount in paise
        order_currency = 'INR'
        order_receipt = str(bill.id)

        # Create order
        razorpay_order = razorpay_client.order.create({
            'amount': order_amount,
            'currency': order_currency,
            'receipt': order_receipt,
            'payment_capture': '1'  # Auto capture
        })

        # Render the payment page with the order ID
        return render(request, 'user/payment.html', {
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_merchant_key': settings.RAZORPAY_API_KEY,
            'amount': order_amount,
            'bill_id': bill.id
        })

    return redirect('payment_history')  # Redirect if not a POST request



@never_cache
@login_required
def payment_success_view(request, bill_id):
    if request.method == 'POST':
        razorpay_order_id = request.POST.get('razorpay_order_id')
        amount = request.POST.get('amount')

        # Verify the payment here (optional but recommended)
        # You can use Razorpay's payment verification API

        # Update the bill status to 'paid'
        bill = get_object_or_404(Bill, id=bill_id, user=request.user.name)
        bill.status = 'paid'
        bill.save()

        return redirect('payment_history')  # Redirect to payment history after success

    return redirect('payment_history')  # Redirect if not a POST request















# views.py
from django.shortcuts import render
from django.http import JsonResponse
from twilio.rest import Client
import json

def send_payment_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_phone = data.get('user_phone')  # User's phone number (WhatsApp)
        service_provider_name = data.get('service_provider_name')  # Service provider's name
        service_provider_upi = data.get('service_provider_upi')  # Service provider's UPI ID
        amount = data.get('amount')  # Amount in INR

        # Prepare the message to send
        message = (
            f"Payment Request from {service_provider_name}:\n"
            f"Total Amount: {amount} INR\n"
            f"Please pay using UPI ID: {service_provider_upi}"
        )

        # Twilio credentials (replace with your actual credentials)
        TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
        TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
        TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Your Twilio WhatsApp number

        # Create a Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        try:
            # Send WhatsApp message
            client.messages.create(
                body=message,
                from_=TWILIO_WHATSAPP_NUMBER,
                to=f'whatsapp:{user_phone}'  # User's WhatsApp number
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})

########################################################################################################

#Admin

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserUpdateForm
from .forms import CustomUserUpdateForm as ProfileUpdateForm
from django.views.decorators.cache import never_cache


@login_required
@never_cache
 # Ensure you import your CustomUser model

def view_users(request):
    # Check if the user is logged in and has the appropriate role
    if 'user_id' in request.session:
        try:
            # Retrieve the user from the session
            user = CustomUser.objects.get(id=request.session['user_id'])
            
            # Check if the user has the 'admin' role or any other necessary permission
            if user.role == 'admin':  # Adjust this condition based on your role management
                users = CustomUser.objects.all() 
                return render(request, 'admin/view_users.html', {'users': users})
            else:
                messages.error(request, "You do not have permission to view this page.")
                return redirect('service_provider_dashboard')  # Redirect to a different page if not authorized
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('login')  # Redirect to login if user not found
    else:
        messages.error(request, "You need to log in to view this page.")
        return redirect('login')  # Redirect to login if session does not exist


# View Profile of admin
def view_profile(request):
    user = request.user
    if user.superuser:  # Custom superuser check
        return render(request, 'admin_dashboard.html', {'user': user})
    else:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('home')

# Update Profile of admin

from django.shortcuts import render, redirect
from .forms import AdminProfileUpdateForm
from .models import CustomUser  # Your custom user model


@never_cache
def admin_dashboard(request):
    if 'admin_id' in request.session:

        user = request.user  # Get the current logged-in user
        context = {
            'user': user,  # Pass the user object to display additional admin info if needed
            'form': AdminProfileUpdateForm(instance=user) 
        }
        return render(request, 'admin/admin_dashboard.html', context)  # Render the dashboard template
    else:
        return redirect('login')


from .forms import AdminProfileUpdateForm
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def admin_profile_update(request):
    user = request.user  # Get the currently logged-in user

    if request.method == 'POST':
        form = AdminProfileUpdateForm(request.POST, instance=user)  # Bind the form to the user instance
        if form.is_valid():
            form.save()  # Save the changes
            messages.success(request, 'Your profile has been updated.')
            return redirect('admin_profile_update')  # Redirect to the dashboard or desired page
    else:
        form = AdminProfileUpdateForm(instance=user)
          # Create a form instance with the user data

    return render(request, 'admin/admin_dashboard.html', {'form': form})

#view users by admin
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def view_users(request):
    users = CustomUser.objects.all()  # Fetch all users
    return render(request, 'admin/view_users.html', {'users': users})

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import CustomUser
from .utils import send_activation_email  # Import the email function
from django.views.decorators.cache import never_cache

@never_cache
def toggle_active_status(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        current_table = request.POST.get('current_table')  # Get the current table (users or service providers)
        
        if status == 'deactivate':
            user.is_active = False
            action = 'deactivated'
        elif status == 'activate':
            user.is_active = True
            action = 'activated'
        
        user.save()
        
        # Send email notification
        send_activation_email(user, action)

        # Redirect back to the same page with the correct table
        if current_table == 'users':
            return redirect('/admin_dashboard?show=users')
        elif current_table == 'service_providers':
            return redirect('/admin_dashboard?show=service_providers')
    
    return redirect('view_users')  # Fallback if something goes wrong

from django.views.decorators.cache import never_cache

@never_cache
def service_provider_list(request):
    # Fetch all service providers along with their related service type
    users = CustomUser.objects.prefetch_related('serviceprovider_set__service_type').all()
    print(users)  # Check if users are being fetched

    return render(request, 'service_provider/serviceprovider_dashboard.html', {
        'users': users,
    })

#add edit delete service type
from django.shortcuts import render, redirect
from .models import ServiceType
from .forms import ServiceTypeForm
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def manage_service_types(request):
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service type added successfully.')
            return redirect('manage_service_types')
    else:
        form = ServiceTypeForm()
    
    service_types = ServiceType.objects.all()
    return render(request, 'admin/manage_service_types.html', {'form': form, 'service_types': service_types})

from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceType
from .forms import ServiceTypeForm
from django.views.decorators.cache import never_cache

@never_cache
def edit_service_type(request, servicetype_id):
    service_type = get_object_or_404(ServiceType, servicetype_id=servicetype_id)
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST, request.FILES, instance=service_type)
        if form.is_valid():
            form.save()
            messages.success(request, f"Service type '{service_type.servicetype_name}'updated successfully.")
            return redirect('manage_service_types')
    else:
        form = ServiceTypeForm(instance=service_type)
    return render(request, 'admin/manage_service_types.html', {'form': form, 'service_type': service_type})

from django.views.decorators.cache import never_cache

@never_cache
def delete_service_type(request, servicetype_id):
    service_type = get_object_or_404(ServiceType, servicetype_id=servicetype_id)
    if request.method == 'POST':
        service_type.delete()
        messages.success(request, f'Service type "{service_type.servicetype_name}" deleted successfully.')
        return redirect('manage_service_types')
    return redirect('manage_service_types')


 #add edit delete service category

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ServiceTypeCategoryForm
from .models import ServiceTypeCategory, ServiceType
from django.views.decorators.cache import never_cache

@never_cache
def manage_service_categories(request):
    if request.method == 'POST':
        form = ServiceTypeCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service category added successfully.')
            return redirect('manage_service_categories')
    else:
        form = ServiceTypeCategoryForm()
    
    categories = ServiceTypeCategory.objects.all()
    service_types = ServiceType.objects.all()
    
    return render(request, 'admin/manage_service_category.html', {
        'form': form,
        'categories': categories,
        'service_types': service_types
    })

from django.views.decorators.cache import never_cache

@never_cache
def edit_service_category(request, category_id):
    category = get_object_or_404(ServiceTypeCategory, category_id=category_id)
    if request.method == 'POST':
        form = ServiceTypeCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service category updated successfully.')
            return redirect('manage_service_categories')
    return redirect('manage_service_categories')

from django.views.decorators.cache import never_cache

@never_cache
def delete_service_category(request, category_id):
    category = get_object_or_404(ServiceTypeCategory, category_id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Service category deleted successfully.')
    return redirect('manage_service_categories')



########################################################################################################



# #Service Provider
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import CustomUser, ServiceProvider, Booking
from .forms import CustomUserUpdateForm
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from .models import ServiceProvider, Booking 

@never_cache
def service_provider_dashboard(request):
    """
    Service provider dashboard view showing summary of requests and services
    """
    try:
        service_provider = ServiceProvider.objects.select_related('service_type').get(user=request.user)
        
        # Get counts for different request statuses
        pending_requests = Booking.objects.filter(
            service_provider=service_provider,
            status='pending'
        ).count()
        
        ongoing_services = Booking.objects.filter(
            service_provider=service_provider,
            status='ongoing'
        ).count()
        
        completed_services = Booking.objects.filter(
            service_provider=service_provider,
            status='completed'
        ).count()

        accepted_services = Booking.objects.filter(
            service_provider=service_provider,
            status='accepted'
        ).count()

        # Get recent requests
        recent_requests = Booking.objects.filter(
            service_provider=service_provider
        ).order_by('-created_at')[:5]

        context = {
            'user': request.user,
            'service_provider': service_provider,
            'pending_requests_count': pending_requests,
            'ongoing_services_count': ongoing_services,
            'completed_services_count': completed_services,
            'accepted_services_count': accepted_services,
            'recent_requests': recent_requests
        }
        
    except ServiceProvider.DoesNotExist:
        messages.error(request, 'Service Provider profile not found.')
        context = {
            'user': request.user,
            'pending_requests_count': 0,
            'ongoing_services_count': 0,
            'completed_services_count': 0,
            'accepted_services_count': 0
        }

    return render(request, 'service_provider/serviceprovider_dashboard.html', context)    
@never_cache
def service_provider_dashboard(request):
    """
    Service provider dashboard view showing summary of requests and services
    """
    try:
        service_provider = ServiceProvider.objects.select_related('service_type').get(user=request.user)
        
        # Get counts for different request statuses
        pending_requests = Booking.objects.filter(
            service_provider=service_provider,
            status='pending'
        ).count()
        
        ongoing_services = Booking.objects.filter(
            service_provider=service_provider,
            status='ongoing'
        ).count()
        
        completed_services = Booking.objects.filter(
            service_provider=service_provider,
            status='completed'
        ).count()

        accepted_services = Booking.objects.filter(
            service_provider=service_provider,
            status='accepted'
        ).count()

        # Get recent requests
        recent_requests = Booking.objects.filter(
            service_provider=service_provider
        ).order_by('-created_at')[:5]

        context = {
            'user': request.user,
            'service_provider': service_provider,
            'pending_requests_count': pending_requests,
            'ongoing_services_count': ongoing_services,
            'completed_services_count': completed_services,
            'accepted_services_count': accepted_services,
            'recent_requests': recent_requests
        }
        
    except ServiceProvider.DoesNotExist:
        messages.error(request, 'Service Provider profile not found.')
        context = {
            'user': request.user,
            'pending_requests_count': 0,
            'ongoing_services_count': 0,
            'completed_services_count': 0,
            'accepted_services_count': 0
        }

    return render(request, 'service_provider/serviceprovider_dashboard.html', context)


from django.http import JsonResponse

@login_required
def accept_booking(request, booking_id):
    """
    Accept a booking request and update the booking with the service provider's location
    """
    if request.method == 'POST':
        try:
            booking = Booking.objects.get(id=booking_id, service_provider__user=request.user)
            booking.status = 'accepted'
            
            # Get the live location from the request
            live_location = request.POST.get('live_location')
            booking.service_provider_location = live_location  # Store the live location
            booking.save()

            messages.success(request, 'Booking accepted successfully!')

            return JsonResponse({'status': 'success', 'message': 'Booking accepted successfully!'})

        except Booking.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Booking not found or you do not have permission to accept it.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

from django.shortcuts import render
from django.contrib import messages
from .models import ServiceProvider, Bill  # Ensure you import your Bill model

def view_payments(request):
    """
    View to display payments sent by the service provider.
    """
    try:
        service_provider = ServiceProvider.objects.get(user=request.user)
        
        # Retrieve bills associated with the service provider
        payments = Bill.objects.filter(service_provider=service_provider.user.name).order_by('-created_at')  # Adjust the field as necessary

        context = {
            'payments': payments,
            'user': request.user,
        }
        
    except ServiceProvider.DoesNotExist:
        messages.error(request, 'Service Provider profile not found.')
        context = {
            'payments': [],
            'user': request.user,
        }

    return render(request, 'service_provider/view_payment.html', context)
@never_cache
@login_required
def view_requests(request):
    """
    View to display service requests based on their status
    """
    try:
        service_provider = ServiceProvider.objects.get(user=request.user)
        status = request.GET.get('status', 'all')
        
        # Base query
        bookings = Booking.objects.filter(service_provider=service_provider)
        
        # Apply status filter
        if status != 'all':
            bookings = bookings.filter(status=status)
        
        # Get counts for the summary
        context = {
            'bookings': bookings.order_by('-created_at'),
            'current_status': status,
            'pending_count': Booking.objects.filter(service_provider=service_provider, status='pending').count(),
            'ongoing_count': Booking.objects.filter(service_provider=service_provider, status='ongoing').count(),
            'completed_count': Booking.objects.filter(service_provider=service_provider, status='completed').count(),
            'accepted_count': Booking.objects.filter(service_provider=service_provider, status='accepted').count(),
            'user': request.user,
            'service_provider': service_provider
        }
        
    except ServiceProvider.DoesNotExist:
        messages.error(request, 'Service Provider profile not found.')
        return redirect('service_provider_dashboard')
    
    return render(request, 'service_provider/view_requests.html', context)

@never_cache
@login_required
def update_profile(request):
    """
    Handle service provider profile updates
    """
    try:
        service_provider = ServiceProvider.objects.select_related('service_type').get(user=request.user)
        
        if request.method == 'POST':
            form = CustomUserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('service_provider_dashboard')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CustomUserUpdateForm(instance=request.user)
            
        context = {
            'form': form,
            'service_provider': service_provider,
        }
        
    except ServiceProvider.DoesNotExist:
        messages.error(request, 'Service Provider profile not found.')
        return redirect('service_provider_dashboard')
        
    return render(request, 'service_provider/serviceprovider_dashboard.html', context)

@login_required
def booking_status_update(request, booking_id, new_status):
    """
    Generic view to handle booking status updates
    """
    try:
        booking = get_object_or_404(Booking, 
             id=booking_id, 
             service_provider__user=request.user)
        
        # Define valid status transitions
        valid_transitions = {
            'pending': ['accepted'],
            'accepted': ['ongoing'],
            'ongoing': ['completed']
        }
        
        if new_status in valid_transitions.get(booking.status, []):
            booking.status = new_status
            booking.save()
            
            status_messages = {
                'accepted': 'Booking accepted successfully.',
                'ongoing': 'Service started successfully.',
                'completed': 'Service completed successfully.'
            }
            messages.success(request, status_messages[new_status])
        else:
            messages.error(request, f'Invalid status transition from {booking.status} to {new_status}')
            
    except Booking.DoesNotExist:
        messages.error(request, 'Booking not found.')
        
    return redirect('view_requests')

# Specific status update views
@login_required
def accept_booking(request, booking_id):
    return booking_status_update(request, booking_id, 'accepted')

@login_required
def start_service(request, booking_id):
    return booking_status_update(request, booking_id, 'ongoing')

@login_required
def complete_service(request, booking_id):
    return booking_status_update(request, booking_id, 'completed')


#view service history
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def view_service_history(request):
    # Get all completed bookings for the current service provider
    service_history = Booking.objects.filter(
        service_provider__user=request.user,
        status='completed'
    ).order_by('-created_at')
    
    context = {
        'service_history': service_history
    }
    return render(request, 'service_provider/service_history.html', context)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Feedback, ServiceProvider

@login_required
def view_feedback(request):
    try:
        service_provider = ServiceProvider.objects.get(user=request.user)
        feedbacks = Feedback.objects.filter(service_provider=service_provider).order_by('-timestamp')
        context = {
            'feedbacks': feedbacks
        }
        return render(request, 'service_provider/view_feedback.html', context)
    except ServiceProvider.DoesNotExist:
        messages.error(request, "You are not registered as a service provider.")
        return redirect('serviceprovider_dashboard')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, ServiceProvider  # Ensure you import the necessary models

def bill_view(request, booking_id):
    # Get the booking details
    booking = get_object_or_404(Booking, id=booking_id)
    
    # Fetch the service provider associated with the booking
    service_provider = booking.service_provider

    charge = booking.service_type_category.charge

    # Render the bill form with booking details
    return render(request, 'service_provider/bill.html', {
        'booking': booking,
        'user': booking.user,
        'service_provider': service_provider,
        'charge':charge
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, Bill 
import re  # Import the regular expressions module

def submit_bill(request, booking_id):
    # Fetch the booking details using the booking_id
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Fetching details from the booking instance
        user = booking.user.name  # Fetch the username from the booking instance
        service_provider = booking.service_provider.user.name  # Fetch the service provider's name
        service_type = booking.service_type_category.category_name  # Fetch the service type name
        
        # Extract numeric value from charge string
        charge_str = booking.service_type_category.charge
        charge = float(re.search(r"[\d.]+", charge_str).group())  # Extract the numeric part

        # Get the additional inputs from the form
        try:
            kilometers = float(request.POST.get('kilometers', 0))  # Default to 0 if not provided
            additional_charge = float(request.POST.get('additional_charge', 0))  # Default to 0 if not provided
        except ValueError:
            messages.error(request, 'Invalid input for kilometers or additional charge.')
            return redirect('bill_view', booking_id=booking_id)

        # Calculate the total amount
        total_amount = (charge * kilometers) + additional_charge

        # Create a new Bill instance and save it to the database
        Bill.objects.create(
            user=user,
            service_provider=service_provider,
            service_type=service_type,
            charge=charge,
            kilometers=kilometers,
            additional_charge=additional_charge,
            total_amount=total_amount
        )

        messages.success(request, 'Bill submitted successfully!')
        return redirect('service_provider_dashboard')  # Redirect to a relevant page after submission

    # If the request method is not POST, redirect to the bill view
    return redirect('bill_view', booking_id=booking_id)



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Bill

def get_bill_details(request, booking_id):
    bill = get_object_or_404(Bill, booking_id=booking_id)  # Adjust as necessary
    data = {
        'user': bill.user.name,
        'service_provider': bill.service_provider.user.name,
        'service_type': bill.service_type,
        'charge': bill.charge,
        'kilometers': bill.kilometers,
        'additional_charge': bill.additional_charge,
        'total_amount': bill.total_amount,
    }
    return JsonResponse(data)






###########################################################################################################


# from django.http import JsonResponse
# import re
# import json
# import random

# def chatbot_response(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             user_message = data.get('message', '').lower()
            

#             # Vehicle knowledge base responses
#             responses = {
#                 # Engine Systems
#                 r'engine.*start': {
#                     'responses': [
#                         "Based on your description, here are possible reasons why your engine won't start:\n"
#                         "1. Dead battery (most common)\n"
#                         "2. Faulty starter motor\n"
#                         "3. Fuel system issues\n"
#                         "4. Ignition switch problems\n\n"
#                         "Do you hear any specific sound when trying to start?",
                        
#                         "Let's diagnose your engine start problem:\n"
#                         "1. If you hear clicking: Likely battery issue\n"
#                         "2. If there's no sound: Could be ignition switch\n"
#                         "3. If engine cranks but won't start: Possibly fuel system\n\n"
#                         "Which symptom matches your situation? Please respond with the number."
#                     ]
#                 },
#                 # Battery Issues
#                 r'battery|jump.*start': {
#                     'responses': [
#                         "Here's how to safely jump-start your car:\n"
#                         "1. Position cars close, both turned off\n"
#                         "2. Connect RED cable to POSITIVE (+) of dead battery\n"
#                         "3. Connect other RED end to POSITIVE (+) of good battery\n"
#                         "4. Connect BLACK cable to NEGATIVE (-) of good battery\n"
#                         "5. Connect other BLACK end to unpainted metal in dead car\n"
#                         "6. Start working car, wait 2 minutes\n"
#                         "7. Try starting dead car\n\n"
#                         "Need more specific instructions? Please respond with the number.",
#                     ]
#                 },
#                 # Transmission Problems
#                 r'transmission|gear|shift': {
#                     'responses': [
#                         "Common transmission problems include:\n"
#                         "1. Delayed/rough shifting\n"
#                         "2. Grinding or shaking\n"
#                         "3. Burning smell\n"
#                         "4. Transmission fluid leaks\n\n"
#                         "Which symptoms are you experiencing? Please respond with the number.",
#                     ]
#                 },
#                 # Brake System
#                 r'brake|stop': {
#                     'responses': [
#                         "Brake system warning signs:\n"
#                         "1. Squealing/squeaking: Worn brake pads\n"
#                         "2. Grinding: Metal-on-metal contact\n"
#                         "3. Vibration: Warped rotors\n"
#                         "4. Soft pedal: Possible fluid leak\n\n"
#                         "Which symptom are you experiencing? Please respond with the number.",
#                     ]
#                 },
#                 # Tire Issues
#                 r'tire|flat|pressure': {
#                     'responses': [
#                         "Tire maintenance guide:\n"
#                         "1. Correct pressure: Check when cold\n"
#                         "2. Rotation: Every 5,000-8,000 miles\n"
#                         "3. Alignment: If pulling to one side\n"
#                         "4. Tread depth: Use penny test\n\n"
#                         "Need specific instructions for any of these? Please respond with the number.",
#                     ]
#                 },
#                 # Maintenance
#                 r'maintenance|service': {
#                     'responses': [
#                         "Regular maintenance schedule:\n"
#                         "1. Oil & filter: 3,000-7,500 miles\n"
#                         "2. Tire rotation: 5,000-8,000 miles\n"
#                         "3. Air filter: 15,000-30,000 miles\n"
#                         "4. Brake fluid: Every 2 years\n"
#                         "5. Coolant: Every 30,000 miles\n\n"
#                         "Need specific service details? Please respond with the number.",
#                     ]
#                 },
#                 # Check Engine Light
#                 r'check.*engine|warning.*light': {
#                     'responses': [
#                         "Common check engine light causes:\n"
#                         "1. Loose gas cap\n"
#                         "2. Oxygen sensor failure\n"
#                         "3. Catalytic converter issues\n"
#                         "4. Spark plug/wire problems\n\n"
#                         "Which one do you think it might be? Please respond with the number.",
#                     ]
#                 },
#                 # Fluid Leaks
#                 r'leak|fluid|oil': {
#                     'responses': [
#                         "Identify fluid leaks by color:\n"
#                         "1. Red: Transmission fluid\n"
#                         "2. Brown/black: Engine oil\n"
#                         "3. Green/orange: Coolant\n"
#                         "4. Clear/brown: Brake fluid\n"
#                         "5. Clear: Water (likely AC)\n\n"
#                         "What color is the leak you're seeing? Please respond with the number.",
#                     ]
#                 }
#             }

#             # Follow-up responses for specific issues
#             follow_up_responses = {
#                 'engine': [
#                     "To check the battery, look for corrosion on terminals and ensure connections are tight.",
#                     "If you suspect a starter issue, try tapping it gently while someone turns the key.",
#                     "If fuel system issues are suspected, check for fuel leaks or listen for the fuel pump.",
#                     "For ignition switch problems, try turning the key to the 'on' position and see if the dashboard lights come on."
#                 ],
#                 'battery': [
#                     "For jump-starting, ensure both cars are off before connecting cables.",
#                     "If the battery is old, consider replacing it after jump-starting."
#                 ],
#                 'transmission': [
#                     "Check the transmission fluid level and color; it should be red and not smell burnt.",
#                     "If you hear grinding noises, it may indicate a serious issue that needs immediate attention."
#                 ],
#                 'brake': [
#                     "Check the brake fluid level; it should be between the minimum and maximum marks.",
#                     "If you hear squeaking, it might be time to replace the brake pads."
#                 ],
#                 'tire': [
#                     "To check tire pressure, use a gauge; it should match the recommended PSI in your manual.",
#                     "For a flat tire, ensure you have a spare and the necessary tools before starting."
#                 ],
#                 'maintenance': [
#                     "For oil changes, check your manual for the recommended interval based on your driving habits.",
#                     "Make sure to rotate your tires regularly to ensure even wear."
#                 ],
#                 'check_engine': [
#                     "You can get the error code read at most auto parts stores for free.",
#                     "If the light is flashing, it indicates a serious issue; consider stopping the vehicle."
#                 ],
#                 'leak': [
#                     "If you see red fluid, it's likely transmission fluid; check for leaks under the vehicle.",
#                     "For brown fluid, it could be engine oil; monitor the level and consider a mechanic."
#                 ]
#             }

#             # Check for gratitude messages
#             gratitude_phrases = [
#                 "thanks", "thank you", "ok thanks", "well it worked", 
#                 "thanks bud", "thanks buddy", "thank you so much", 
#                 "appreciate it", "cheers", "thanks a lot", "it worked",
#                 "Much obliged", "Many thanks", "Thanks heaps",
#                 "Thanks a ton", "Big thanks", "Thanks kindly",
#                 "Thanks a million", "I'm grateful", "Grateful for your help",
#                 "Deeply appreciated", "Thanks indeed", "Thanks for that",
#                 "Ta", "Thanks a bunch", "You're the best", "Kudos",
#                 "Thanks so very much", "Thanks for your support",
#                 "Hats off to you", "Many, many thanks",
#                 "Couldn't have done it without you", "You're a lifesaver",
#                 "Thank you kindly",
#             ]

#             # Check if the user message contains any gratitude phrases
#             if any(phrase in user_message for phrase in gratitude_phrases):
#                 return JsonResponse({
#                     'response': "You're welcome! 😊 Let me know if you have more questions or need further help. Good luck! 🚀"
#                 })
            
#             # Check for matches and return random response from matching category
#             for pattern, response_data in responses.items():
#                 if re.search(pattern, user_message):
#                     return JsonResponse({
#                         'response': random.choice(response_data['responses'])
#                     })

#             # Check for follow-up queries
#             if user_message.isdigit():
#                 user_input = int(user_message)
#                 # Determine the context from the previous question
#                 if 'check engine' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['check_engine'][user_input - 1] if user_input in [1, 2, 3, 4] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'engine' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['engine'][user_input - 1] if user_input in [1, 2, 3, 4] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'battery' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['battery'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'transmission' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['transmission'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'brake' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['brake'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'tire' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['tire'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'maintenance' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['maintenance'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })
#                 elif 'leak' in user_message:
#                     return JsonResponse({
#                         'response': follow_up_responses['leak'][user_input - 1] if user_input in [1, 2] else "For more information and to solve the issue, it's best to call a mechanic. What would you like to do next?"
#                     })

#             # Default response for unmatched queries
#             default_responses = [
#                 "I'm not sure about that. Could you ask about specific vehicle issues? I can help with:\n"
#                 "• Engine problems\n"
#                 "• Battery issues\n"
#                 "• Transmission concerns\n"
#                 "• Brake problems\n"
#                 "• Tire maintenance",

#                 "I specialize in vehicle-related questions. Please ask about:\n"
#                 "• Warning lights\n"
#                 "• Strange noises\n"
#                 "• Maintenance schedules\n"
#                 "• Fluid leaks\n"
#                 "• General car care",

#                 "I'm your vehicle assistant. Try asking about:\n"
#                 "• Starting problems\n"
#                 "• Performance issues\n"
#                 "• Regular maintenance\n"
#                 "• Safety concerns\n"
#                 "• Basic repairs"
#             ]

#             return JsonResponse({
#                 'response': random.choice(default_responses)
#             })

#         except json.JSONDecodeError:
#             return JsonResponse({
#                 'response': "Sorry, I couldn't process that request. Please try again."
#             })
#         except Exception as e:
#             return JsonResponse({
#                 'response': "An error occurred. Please try again later."
#             })

#     return JsonResponse({
#         'error': 'Invalid request method'
#     })


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import google.generativeai as genai
import json

# Configure logging
logger = logging.getLogger(__name__)

# Set your Gemini API Key
API_KEY = "AIzaSyDeGoQyD0YL2T9nCb33tzOKv0YzzbXStUw"

# Configure the Generative AI client
genai.configure(api_key=API_KEY)

# Define allowed keywords related to vehicle issues
ALLOWED_KEYWORDS = [
    "engine", "battery", "transmission", "brake", "tire", "maintenance",
    "check engine", "warning light", "fluid leak", "oil", "vehicle", "car",
    "alternator", "radiator", "spark plug", "fuel pump", "exhaust", "coolant",
    "air filter", "timing belt", "clutch", "suspension", "shock absorber",
    "steering", "alignment", "wheel", "axle", "differential", "catalytic converter",
    "muffler", "headlight", "taillight", "windshield", "wiper", "dashboard",
    "odometer", "speedometer", "gearbox", "ignition", "starter", "fan belt",
    "brake pad", "rotor", "caliper", "master cylinder", "power steering",
    "fuel injector", "turbocharger", "supercharger", "thermostat", "heater",
    "air conditioning", "AC", "defroster", "emission", "diagnostic", "OBD",
    "tune-up", "service", "inspection", "repair", "overheating", "stalling",
    "vibration", "noise", "leak", "smoke", "jerking", "hesitation", "rough idle",
    "hi", "hello", "mercedes", "audi", "bmw", "toyota", "honda", "ford", "chevrolet",
    "nissan", "hyundai", "kia", "volkswagen", "subaru", "mazda", "jeep", "dodge",
    "lexus", "infiniti", "acura", "volvo", "jaguar", "land rover", "porsche", "tesla",
    "bike", "motorcycle", "scooter", "moped", "bicycle", "truck", "lorry", "bus",
    "van", "minivan", "pickup", "SUV", "sedan", "convertible", "coupe", "hatchback",
    "wagon", "limousine", "ambulance", "fire truck", "police car", "taxi", "cab",
    "tractor", "trailer", "RV", "camper", "caravan", "forklift", "bulldozer",
    "excavator", "crane", "cement mixer", "garbage truck", "tow truck", "delivery van"
    "honda", "yamaha", "suzuki", "kawasaki", "ducati", "harley-davidson",
    "bmw", "ktm", "triumph", "aprilia", "royal enfield", "bajaj", "hero",
    "tvs", "mahindra", "indian", "husqvarna", "benelli", "mv agusta",
    "vespa", "piaggio", "guzzi", "norton", "bimota", "cagiva", "laverda",
    "moto morini", "kymco", "sym", "cfmoto", "zero", "energica", "lightning",
    "alta", "brammo", "victory", "can-am", "polaris", "ural", "bsa", "jawa",
    "aermacchi", "gilera", "derbi", "montesa", "ossa", "sherco", "gas gas",
    "beta", "tm racing", "husaberg", "atala", "bultaco", "zundapp", "puch",
    "sachs", "mz", "simson", "cz", "jawa", "tork", "revolt", "ather", "ola"
]

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message').lower()

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            # Check if the message contains any allowed keywords
            if not any(keyword in user_message for keyword in ALLOWED_KEYWORDS):
                logger.info(f"Message '{user_message}' does not contain allowed keywords.")
                return JsonResponse({'response': "I'm Road Guardian. Please ask questions or doubts about vehicles."})

            # Create the model
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Generate content using the user message
            response = model.generate_content(user_message)

            # Extract the AI response
            ai_message = response.text

            # Log the AI response for debugging
            logger.info(f"Gemini API response: {ai_message}")

            return JsonResponse({'response': ai_message})

        except Exception as e:
            logger.error(f"Error fetching response from Gemini API: {str(e)}")
            return JsonResponse({'error': 'Failed to get response from AI'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .forms import VehicleForm  # Import the VehicleForm

@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)  # Create the Vehicle instance but don't save yet
            vehicle.user = request.user  # Set the user
            vehicle.save()  # Save the instance to the database

            messages.success(request, 'Vehicle added successfully!')  # Success
            
            return redirect('vehicle_list')  # Redirect to the vehicle list page
        else:
            print(request.POST)  # Check what values are being submitted
    else:
        form = VehicleForm()  # Create a new form instance

    return render(request, 'user/add_vehicle.html', {'form': form})  # Render the form



def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    vehicle.delete()
    return redirect('vehicle_list')


def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, user=request.user)
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    
    return render(request, 'user/edit_vehicle.html', {'form': form, 'vehicle': vehicle})


def vehicle_list(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'user/vehicle_list.html', {'vehicles': vehicles})





#Report Incident View

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncidentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .templatetags.image_detection import detect_ai_image

@login_required  # Add login required decorator
def report_incident(request):
    error_message = None
    success_message = None

    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.user = request.user
            
            image_file = request.FILES['image']
            image_data = image_file.read()
            result = detect_ai_image(image_data)

            if result == 'AI-generated':
                error_message = 'The image appears to be AI-generated. Please upload a real photo.'
            else:
                incident.image = image_file
                incident.save()
                success_message = 'Incident reported successfully!'
                return redirect('user_dashboard')

    else:
        form = IncidentForm()

    return render(request, 'user/report_incident.html', {
        'form': form,
        'error_message': error_message,
        'success_message': success_message
    })

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        image_data = request.body
        result = detect_ai_image(image_data)
        return JsonResponse({'classification': result})
    return JsonResponse({'error': 'Invalid request method'})