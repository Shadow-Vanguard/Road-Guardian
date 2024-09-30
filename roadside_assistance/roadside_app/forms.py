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

# Get the user model (custom or default)
CustomUser = get_user_model()

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'phone', 'address', 'email', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError("This username is already taken.")
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

