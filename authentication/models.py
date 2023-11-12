from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(upload_to="static/images/profile_images", null=True)
    website = models.CharField(max_length=250, null=True)
    instagram = models.CharField(max_length=250, null=True)
    facebook = models.CharField(max_length=250, null=True)
    type_choices = (
        (0, 'Student'),
        (1, 'Instructor')
    )
    type = models.CharField(max_length=1, choices=type_choices)