# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('service_provider', 'Service Provider'),
        
    )
    
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=150,  db_index=True) 

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)  # hashed password
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'address','email', 'role']

    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            
        ]
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        
    # Fix reverse accessor conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
    )


#tbl_service provider

from django.db import models
from .models import CustomUser

class ServiceType(models.Model):
    servicetype_id = models.AutoField(primary_key=True)
    servicetype_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.servicetype_name

class ServiceProvider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True)  # No need to import again
    certificate = models.ImageField(upload_to='certificates/')
    area_of_service = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.name} - {self.service_type.servicetype_name if self.service_type else "No service type"}'
