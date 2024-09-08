from django.db import models

import uuid

from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Tag(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)
    

class Country(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Channel(BaseModel):
    author = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='channel_author')
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)
    link = models.URLField(max_length=225, unique=True, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='channel_image/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)


class Subscription(BaseModel):
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='subscription_user')
    channel = models.ForeignKey(to='Channel', on_delete=models.CASCADE, db_index=True, unique=True, null=True, blank=True, related_name='subscription_channel')

    def __str__(self):
        return f"{self.user}-{self.channel}"
    

class PlayList(BaseModel):
    name = models.CharField(max_length=225, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)


class SubEmail(BaseModel):
    sub_email = models.EmailField(unique=True, max_length=225, db_index=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.sub_email}"
