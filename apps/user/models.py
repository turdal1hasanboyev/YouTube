from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    """User model"""
    bio = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.username
