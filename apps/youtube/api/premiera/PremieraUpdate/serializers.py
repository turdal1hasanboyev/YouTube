from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Premiera


class PremieraUpdateSerializer(ModelSerializer):
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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
