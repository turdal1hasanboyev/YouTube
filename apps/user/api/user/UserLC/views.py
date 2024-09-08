from rest_framework.generics import ListCreateAPIView

from .serializers import UserLCSerializer
from apps.user.models import User


class UserLCView(ListCreateAPIView):
    """
    List all users or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserLCSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)
