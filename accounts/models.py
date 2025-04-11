from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here if needed
    # Example: adding a phone number field
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    pass
    def __str__(self):
        return self.username
