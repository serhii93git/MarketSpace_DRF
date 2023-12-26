from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    add_info = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username
