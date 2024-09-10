from rest_framework.serializers import ModelSerializer

from apps.common.models import Country


class CountryRUDSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            'is_active',
            ]

        extra_kwargs = {
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }
