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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm

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

            if username == 'admin' and password == 'admin123':
                return render(request,'admin/admin_dashboard.html')  # Ensure that 'admin_dashboard' is properly configured in URLs
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_superuser:
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

# Admin dashboard view
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


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




#admin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def view_users(request):
    users = CustomUser.objects.all()  # Fetch all users from the database
    return render(request, 'admin/view_users.html', {'users': users})

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



#password reset
# views.py
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
