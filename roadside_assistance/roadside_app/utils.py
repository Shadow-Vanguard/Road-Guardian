# utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_activation_email(user, action):
    subject = f'Your account has been {action}'
    
    if action == 'activated':
        message = f'Hello {user.name},\n\nYour account has been {action} by the admin.\n\nThank you!'
    elif action == 'deactivated':
        message = f'Hello {user.name},\n\nYour account has been {action} by the admin. If you want to know more please contact the admin.\n\n If you need to contact email as in road.guardian08@gmail.com.\n\n Thank you!'
    else:
        message = f'Hello {user.name},\n\nYour account status has been updated.\n\nThank you!'

    recipient_list = [user.email]

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)