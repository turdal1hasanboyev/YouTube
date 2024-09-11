from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Content

from apps.common.api.tag.TagLC.serializers import TagLCSerializer
from apps.common.api.category.CategoryLC.serializers import CategoryLCSerializer
from apps.common.api.channel.ChannelRetrieve.serializers import ChannelRetrieveSerializer
from apps.common.api.country.CountryLC.serializers import CountryLCSerializer
from apps.common.api.playlist.PlayListLC.serializers import PlayListLCSerializer


class ContentRetrieveSerializer(ModelSerializer):
    tags = TagLCSerializer(many=True, read_only=True)
    category = CategoryLCSerializer(read_only=True)
    channel = ChannelRetrieveSerializer(read_only=True)
    country = CountryLCSerializer(read_only=True)
    play_list = PlayListLCSerializer(read_only=True)

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
