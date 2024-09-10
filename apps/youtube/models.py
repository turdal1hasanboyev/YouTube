from django.db import models

import uuid
from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Content(BaseModel):

    LANGUAGE = (
        ('en', ('English')),
        ('ru', ('Russian')),
        ('uz', ('Uzbek')),
    )

    title = models.CharField(max_length=225, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)
    description = RichTextField(null=True, blank=True)
    link = models.URLField(max_length=225, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='content_image/', null=True, blank=True)
    video = models.FileField(upload_to='content_video/', null=True, blank=True)
    tags = models.ManyToManyField('common.Tag', blank=True)
    category = models.ForeignKey(to='common.Category', on_delete=models.CASCADE, null=True, blank=True, related_name='category_content')
    channel = models.ForeignKey('common.Channel', on_delete=models.CASCADE, null=True, blank=True, related_name='channel_content')
    country = models.ForeignKey(to='common.Country', on_delete=models.CASCADE, null=True, blank=True, related_name='country_content')
    play_list = models.ForeignKey('common.PlayList', on_delete=models.CASCADE, null=True, blank=True, related_name='play_list_content')
    like = models.IntegerField(default=0, null=True, blank=True)
    dislike = models.IntegerField(default=0, null=True, blank=True)
    forward = models.IntegerField(default=0, null=True, blank=True)
    premiere_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=225, choices=LANGUAGE, null=True, blank=True)
    is_short_video = models.BooleanField(default=True, null=True, blank=True)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Liked(BaseModel):

    LIKED = (
        ('like', ('Like')),
        ('dislike', ('Dislike')),
    )

    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='liked_user')
    content = models.ForeignKey(to=Content, on_delete=models.CASCADE, null=True, blank=True, related_name='liked_content')
    liked = models.CharField(max_length=225, choices=LIKED, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.user}-{self.content}-{self.liked}"


class Comment(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True, related_name='comment_content')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='comment_user')
    comment = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.content}-{self.user}"


class SavedForLater(BaseModel):
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='saved_user')
    content = models.ForeignKey(to=Content, on_delete=models.CASCADE, null=True, blank=True, related_name='saved_content')

    def __str__(self):
        return f"{self.id}-{self.user}-{self.content}"


class Premiera(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True, related_name='premiera_content')
    premiere_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.content}-{self.premiere_date}"
