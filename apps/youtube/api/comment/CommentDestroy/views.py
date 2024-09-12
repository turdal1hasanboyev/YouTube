from rest_framework.generics import DestroyAPIView

from apps.youtube.models import Comment
from .serializers import CommentDestroySerializer


class CommentDestroyView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'content')
    
    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()
    