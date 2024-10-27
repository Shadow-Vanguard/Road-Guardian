from urllib import request
from .models import CustomUser

def set_role(backend, user, response, *args, **kwargs):
    custom_user, created = CustomUser.objects.get_or_create(username=user.username)
    print(created)

    if created:
        custom_user.name = user.get_full_name() or user.username
        custom_user.email = user.email or ''
        custom_user.phone = ''  # You might want to add this to the social auth pipeline
        custom_user.address = ''  # You might want to add this to the social auth pipeline

    custom_user.role = 'user'
    custom_user.save()
    session = kwargs['request'].session
    session['user_id'] = user.id
    print(session['user_id'])
    # No need to manually log in or set session variables here
    # Django's auth system will handle this

