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
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Enter Password'}))

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
import re
from django import forms
from .models import CustomUser  # Adjust according to your user model

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'phone', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),      
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
        # Updated regex to allow specific special characters
        if not re.match(r'^[A-Za-z\s.,()]*$', address):
            raise forms.ValidationError("Address must only contain alphabets, periods (.), commas (,), and parentheses (()).")
        return address

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            raise forms.ValidationError("Email must be a valid @gmail.com address.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long.")
        return username
    
from .models import ServiceProvider 
class ServiceProviderLocationUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['location']
        widgets = {
            'location': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your location here...'}),
        }

        def clean_location(self):
            location = self.cleaned_data.get('location')
            # Add any specific validation for location if needed
            return location


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
        fields = ['service_type', 'certificate', 'area_of_service', 'location', 'availability_status']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'certificate': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'area_of_service': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Describe your district here...'}),  # Use a dropdown for districts
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe your location here...'}),
            'availability_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceProviderForm, self).__init__(*args, **kwargs)
        # Ensure the queryset is correctly set when the form is initialized
        self.fields['service_type'].queryset = ServiceType.objects.all()


from django import forms
from .models import ServiceType

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['servicetype_name', 'description', 'image']
        widgets = {
            'servicetype_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

from django import forms
from .models import ServiceTypeCategory


class ServiceTypeCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceTypeCategory
        fields = ['service_type', 'category_name', 'charge']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'charge': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Booking, ServiceTypeCategory

class BookAssistanceForm(forms.ModelForm):
    charge = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Booking
        fields = ['service_type_category', 'charge', 'location', 'description']
        widgets = {
            'service_type_category': forms.Select(attrs={'class': 'form-control'}),
            'charge': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your current location or click on the map icon to select your location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the issue or service needed'}),
        }

    def __init__(self, *args, **kwargs):
        service_provider = kwargs.pop('service_provider', None)
        super(BookAssistanceForm, self).__init__(*args, **kwargs)
        if service_provider:
            self.fields['service_type_category'].queryset = ServiceTypeCategory.objects.filter(service_type=service_provider.service_type)



from django import forms
from .models import Feedback, ServiceProvider, Booking
from django.core.exceptions import ValidationError
import re

class FeedbackForm(forms.ModelForm):
    service_provider = forms.ModelChoiceField(queryset=ServiceProvider.objects.all(), empty_label="Select a Service Provider")
    booking = forms.ModelChoiceField(queryset=Booking.objects.none(), empty_label="Select a Service")

    class Meta:
        model = Feedback
        fields = ['service_provider', 'booking', 'feedback_text', 'rating']
        widgets = {
            'rating': forms.HiddenInput(),
            'feedback_text': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['service_provider'].queryset = ServiceProvider.objects.filter(booking__user=user, booking__status='completed').distinct()
            self.fields['booking'].queryset = Booking.objects.filter(user=user, status='completed')

    def clean_feedback_text(self):
        feedback_text = self.cleaned_data.get('feedback_text')
        if not re.match(r'^[A-Za-z\s]+$', feedback_text):
            raise ValidationError("Please enter only alphabetic characters.")
        return feedback_text


            

from django import forms
from .models import Vehicle
from django.core.exceptions import ValidationError
from datetime import datetime

class VehicleForm(forms.ModelForm):
       class Meta:
           model = Vehicle
           fields = [
               'registration_number',
               'model',
               'road_tax_document',
               'insurance_document',
               'pollution_certificate_document',
               'tax_expiry_date',
               'insurance_expiry_date',
               'pollution_expiry_date'
           ]
           widgets = {
               'tax_expiry_date': forms.DateInput(attrs={'type': 'text'}),
               'insurance_expiry_date': forms.DateInput(attrs={'type': 'text'}),
               'pollution_expiry_date': forms.DateInput(attrs={'type': 'text'}),
           }

def clean_pollution_expiry_date(self):
            date_str = self.cleaned_data.get('pollution_expiry_date')
            if date_str:
                try:
                    # Convert from DD/MM/YYYY to YYYY-MM-DD
                    return datetime.strptime(date_str, '%d/%m/%Y').date()
                except ValueError:
                    raise ValidationError("Date must be in DD/MM/YYYY format.")
            return None  # Return None if the date is empty



from django import forms
from .models import Incident

# Incident Form
class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        exclude = ['user']  # Exclude user field from form
        fields = ['incident_type', 'location', 'description']
        widgets = {
            'incident_type': forms.Select(attrs={'id': 'incident_type', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'id': 'location', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'id': 'description', 'rows': 4, 'class': 'form-control'}),
        }   