from rest_framework.serializers import ModelSerializer

from apps.youtube.models import Premiera


class PremieraDestroySerializer(ModelSerializer):
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
