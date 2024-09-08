from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import UserRUDSerializer
from apps.user.models import User


class UserRUDView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRUDSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return User.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
