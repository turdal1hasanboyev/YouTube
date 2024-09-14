from rest_framework.serializers import ModelSerializer

from apps.youtube.models import SavedForLater

from apps.user.api.user.UserLC.serializers import UserLCSerializer
from apps.youtube.api.content.ContentRetrieve.serializers import ContentRetrieveSerializer


class SavedForLaterRetrieveSerializer(ModelSerializer):
    user = UserLCSerializer(read_only=True)
    content = ContentRetrieveSerializer(read_only=True)

    class Meta:
        model = SavedForLater
        fields = [
            'id',
            'user',
            'content',
            'created_at',
            'updated_at',
            'is_active',
        ]
