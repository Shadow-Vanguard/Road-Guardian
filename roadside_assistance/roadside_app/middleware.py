# middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # If the user is trying to access a protected page
            if request.path not in [reverse('login'), reverse('logout')]:
                messages.error(request, "You need to log in to access the account.")
                return redirect('login')  # Redirect to login page

        response = self.get_response(request)
        return response