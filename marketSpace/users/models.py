from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    phone_number = models.CharField(max_length=13)
    add_info = models.TextField(max_length=1000, blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.pk or self.password != self._original_password:
            self.set_password(self.password)

        super().save(*args, **kwargs)

    def clean(self):

        self._original_password = self.password

    def __str__(self):
        return self.username
