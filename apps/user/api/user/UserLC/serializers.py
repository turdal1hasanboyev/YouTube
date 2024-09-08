from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserLCSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'description',
            'image',
            'phone_number',
            'birth_date',
            'gender',
            'occupation',
            'adress',
            'followers_count',
            'following_count',
            'last_active',
            'favourite_social_network',
            "is_active",
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
