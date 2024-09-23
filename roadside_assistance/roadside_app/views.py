from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.shortcuts import render

from .forms import RegistrationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


from .forms import LoginForm

#  from .models import User 

# def print_hello(request):
#     return HttpResponse("Hello Django")

# def print_hello1(request):
#     return HttpResponse("Hello Roshan")


#login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect based on user role
                if user.is_superuser:  # Check if the user is an admin
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                elif user.role == 'user':
                    return redirect('user_dashboard')  # Redirect to user dashboard
                elif user.role == 'service_provider':
                    return redirect('provider_dashboard')  # Redirect to service provider dashboard
                else:
                    return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


#Registration
def reg_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Registration failed. Please check the details and try again.')
    else:
        form = RegistrationForm()
    
    return render(request, 'reg.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')

    
def admin_dashboard(request):
    return render(request, 'user/admin_dashboard.html')


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm

@login_required
def user_dashboard(request):
    user = request.user  # Get the current logged-in user

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user information
            messages.success(request, 'Your changes have been saved.')
            return redirect('user_dashboard')  # Redirect to display the success message
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserUpdateForm(instance=user)  # Load the current user data into the form

    context = {
        'form': form,
    }
    return render(request, 'user/user_dashboard.html', context)


def update_profile(request):
    return render(request, 'user/update_profile.html')


def  service_provider_dashboard(request):
    return render(request, 'service_provider_dashboard_view.html')
    



class PasswordResetRequestView(PasswordResetView):
    template_name = 'password/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/password_reset/done/'

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = '/reset/done/'

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
    user = request.user  # Get the current logged-in user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user information
            messages.success(request, 'Your changes have been saved.')
            return redirect('user_dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserUpdateForm(instance=user)  # Load the current user data into the form

    return render(request, 'user/user_dashboard.html', {'form': form})

@login_required
def view_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'view_profile.html', context)






#admin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def view_users(request):
    # Logic to fetch users
    return render(request, 'view_users.html')

@login_required
def view_service_providers(request):
    # Logic to fetch service providers
    return render(request, 'view_service_providers.html')

@login_required
def add_service_types(request):
    # Logic to add service types
    return render(request, 'add_service_types.html')

@login_required
def order_items(request):
    # Logic for ordering items
    return render(request, 'order_items.html')

@login_required
def view_feedback(request):
    # Logic to view feedback
    return render(request, 'view_feedback.html')

@login_required
def view_incident_report(request):
    # Logic to view incident reports
    return render(request, 'view_incident_report.html')

@login_required
def manage_orders(request):
    # Logic to manage orders
    return render(request, 'manage_orders.html')

@login_required
def manage_product_details(request):
    # Logic to manage product details
    return render(request, 'manage_product_details.html')

def home(request):
    # Redirect after logout
    return render(request, 'home.html')
