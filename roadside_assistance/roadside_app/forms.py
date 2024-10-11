# forms.py
from django import forms
from .models import CustomUser

from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    class Meta:
        model = CustomUser
        fields = ['name', 'phone', 'address','email', 'role', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'role': forms.Select(choices=CustomUser.ROLE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your full name',
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number',
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your address',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password',
        })
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

#admin update profile
from django import forms
from .models import CustomUser


class AdminProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'address', 'name']  # Ensure all necessary fields are included

#Update user profile
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

# Get the user model (custom or default)
CustomUser = get_user_model()

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'phone', 'address', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[A-Z][a-zA-Z\s]*$', name):
            raise forms.ValidationError("Name must start with a capital letter and only contain alphabets.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        if re.match(r'^(\d)\1{9}$', phone):
            raise forms.ValidationError("Invalid phone number format (e.g., 1111111111 or 0000000000 not allowed).")
        return phone

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not re.match(r'^[A-Za-z\s]*$', address):
            raise forms.ValidationError("Address must only contain alphabets.")
        return address

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            raise forms.ValidationError("Email must be a valid @gmail.com address.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*[A-Z])(?=.*[@#$%^&+=]).{6,}$', password):
            raise forms.ValidationError("Password must contain a capital letter, a special character, and be at least 6 characters long.")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        # Add more username validations if needed
        return username
    
    
#forgot password

from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from .models import CustomUser

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}),
        label="Email Address"
    )
    
    def get_users(self, email):
        """
        Override to return users based on the CustomUser model.
        """
        return CustomUser.objects.filter(email__iexact=email, is_active=True)

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
    )

from django import forms
from .models import ServiceProvider, ServiceType

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['service_type', 'certificate', 'area_of_service', 'availability_status']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'area_of_service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter service area'}),
            'availability_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceProviderForm, self).__init__(*args, **kwargs)
        # Ensure the queryset is correctly set when the form is initialized
        self.fields['service_type'].queryset = ServiceType.objects.all()

