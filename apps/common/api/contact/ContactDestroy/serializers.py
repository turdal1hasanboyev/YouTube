from rest_framework.serializers import ModelSerializer

from apps.common.models import Contact


class ContactDestroySerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'author',
            'message',
            'web_site',
            'email',
            'phone_number',
            'is_active',
            'created_at',
            'updated_at',
        ]
