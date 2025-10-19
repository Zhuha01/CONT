from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    profile_picture_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,  # Додаємо null=True для гнучкості
        verbose_name="URL фото профілю"
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()