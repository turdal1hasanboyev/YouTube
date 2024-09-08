from django.db import models

from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class User(BaseModel, AbstractUser):
    """
    User model
    """

    GENDER = (
        ('male', ('Male')),
        ('female', ('Female')),
    )

    OCCUPATION = (
        ('student', ('Student')),
        ('worker', ('Worker')),
    )

    FAVOURITE_SOCIAL_NETWORK = (
        ('telegram', ('Telegram')),
        ('instagram', ('Instagram')),
        ('youtube', ('YouTube')),
    )

    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    phone_number = models.CharField(max_length=225, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=225, null=True, blank=True)
    occupation = models.CharField(choices=OCCUPATION, max_length=225, null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    followers_count = models.IntegerField(default=0, null=True, blank=True)
    following_count = models.IntegerField(default=0, null=True, blank=True)
    last_active = models.DateField(null=True, blank=True)
    favourite_social_network = models.CharField(choices=FAVOURITE_SOCIAL_NETWORK, max_length=225, null=True, blank=True)

    def __str__(self):
        if self.get_full_name():
            return f"{self.id}-{self.get_full_name()}"
        
        elif self.email:
            return f"{self.id}-{self.email}"
        
        return f"{self.id}-{self.username}"
    

class FriendRequest(BaseModel):
    """
    Friend request model
    """

    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='receiver_requests')

    def __str__(self):
        return f"{self.id}-{self.sender}-{self.receiver}"
