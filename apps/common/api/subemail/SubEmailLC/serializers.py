from rest_framework.serializers import ModelSerializer

from apps.common.models import SubEmail


class SubEmailLCSerializer(ModelSerializer):
    class Meta:
        model = SubEmail
        fields = [
            'id',
            'sub_email',
            'created_at',
            'updated_at',
            'is_active',
            ]

        extra_kwargs = {
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }
