from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Premiera

from apps.youtube.api.content.ContentRetrieve.serializers import ContentRetrieveSerializer


class PremieraRetrieveSerializer(ModelSerializer):
    content = ContentRetrieveSerializer(read_only=True)

    class Meta:
        model = Premiera
        fields = [
            'id',
            'content',
            'premiere_date',
            'created_at',
            'updated_at',
            'is_active',
        ]
