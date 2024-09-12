from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Content


class ContentDestroySerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'link',
            'image',
            'video',
            'tags',
            'category',
            'channel',
            'country',
            'play_list',
            'like',
            'dislike',
            'views',
            'forward',
            'premiere_date',
            'language',
            'is_short_video',
            'is_active',
            'created_at',
            'updated_at',
        ]
