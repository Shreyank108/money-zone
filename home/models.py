from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Founder(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="static/images/founder")
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
