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


# # forms.py
# from django import forms
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth import get_user_model

# class CustomPasswordResetForm(PasswordResetForm):
#     email = forms.EmailField(
#         label="Email",
#         max_length=254,
#         widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
#     )

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         User = get_user_model()
#         if not User.objects.filter(email=email).exists():
#             raise forms.ValidationError("No user with this email address exists.")
#         return email

# # forms.py
# from django.contrib.auth.forms import SetPasswordForm
# from django.contrib.auth import get_user_model

# class CustomSetPasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(
#         label="New password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}),
#     )
#     new_password2 = forms.CharField(
#         label="Confirm new password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
#     )


# forms.py
# forms.py
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

# forms.py

from django import forms
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
            'role': forms.Select(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username
