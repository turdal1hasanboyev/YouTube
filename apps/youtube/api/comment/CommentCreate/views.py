from rest_framework.generics import CreateAPIView

from apps.youtube.models import Comment
from .serializers import CommentCreateSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.filter(is_active=True).select_related('user', 'content')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    