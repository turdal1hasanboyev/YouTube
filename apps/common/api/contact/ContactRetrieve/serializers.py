from rest_framework.serializers import ModelSerializer

from apps.common.models import Contact
from apps.user.api.user.UserLC.serializers import UserLCSerializer


class ContactRetrieveSerializer(ModelSerializer):
    author = UserLCSerializer(read_only=True)

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
