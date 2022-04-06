from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True
    )
    password = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    bio = models.TextField(
        blank=True
    )
    is_subscribed = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

User = get_user_model()