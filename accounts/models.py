from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

USER_ROLES = (
    ('PATIENT', 'Patient'),
    ('DOCTOR', 'Doctor'),
)

BLOG_CATEGORIES = (
    ('MENTAL_HEALTH', 'Mental Health'),
    ('HEART_DISEASE', 'Heart Disease'),
    ('COVID19', 'Covid-19'),
    ('IMMUNIZATION', 'Immunization'),
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


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=BLOG_CATEGORIES)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'DOCTOR'})
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_truncated_summary(self, word_limit=15):
        """Return summary truncated to specified word limit"""
        words = self.summary.split()
        if len(words) <= word_limit:
            return self.summary
        return ' '.join(words[:word_limit]) + '...'
