from rest_framework.serializers import ModelSerializer

from apps.youtube.models import SavedForLater


class SavedForLaterDestroySerializer(ModelSerializer):
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
