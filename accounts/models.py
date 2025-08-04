from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = (
    ('PATIENT', 'Patient'),
    ('DOCTOR', 'Doctor'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    REQUIRED_FIELDS = ['email', 'role', 'first_name', 'last_name']
