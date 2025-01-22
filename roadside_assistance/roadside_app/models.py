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

#tbl to add service type by admin

from django.db import models

class ServiceType(models.Model):
    servicetype_id = models.AutoField(primary_key=True)
    servicetype_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='service_types/', null=True, blank=True)

    def __str__(self):
        return self.servicetype_name

# ServiceProvider model (For service providers registering in the system)
from django.conf import settings
from django.db import models

class ServiceProvider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to CustomUser
    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, null=True)  # Service type can be null if removed
    certificate = models.ImageField(upload_to='certificates/')  # Certificate upload field
    area_of_service = models.CharField(max_length=255)  # Area of service as text
    location = models.TextField(default='')   # Field to store location details as text
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        # Checks if the service type is available before displaying it
        return f'{self.user.name} - {self.service_type.servicetype_name if self.service_type else "No service type"}'


from django.db import models


class ServiceTypeCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='categories')
    category_name = models.CharField(max_length=100)
    charge = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.service_type.servicetype_name} - {self.category_name}"

    class Meta:
        verbose_name_plural = "Service Type Categories"


from django.db import models
from django.conf import settings

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service_type_category = models.ForeignKey(ServiceTypeCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.user.name} with {self.service_provider.user.name} at {self.location}"


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks_given')
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='feedbacks_received')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='feedback')
    feedback_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.name} for {self.service_provider.user.name}"
    
from django.db import models

class Bill(models.Model):
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    )

    user = models.CharField(max_length=255)
    service_provider = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    kilometers = models.DecimalField(max_digits=10, decimal_places=2)
    additional_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # New status field

    def __str__(self):
        return f"Bill for {self.user} - {self.service_type}"
    


# roadside_assistance/roadside_app/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    road_tax_document = models.FileField(upload_to='documents/tax/', null=True, blank=True)
    insurance_document = models.FileField(upload_to='documents/insurance/', null=True, blank=True)
    pollution_certificate_document = models.FileField(upload_to='documents/pollution/', null=True, blank=True)
    tax_expiry_date = models.DateField(null=True, blank=True)
    insurance_expiry_date = models.DateField(null=True, blank=True)
    pollution_expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.registration_number} - {self.model}"