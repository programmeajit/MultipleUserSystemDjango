from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_job_seeker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='job_seeker')
    # Add additional fields as needed

class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employer')
    # Add additional fields as needed

