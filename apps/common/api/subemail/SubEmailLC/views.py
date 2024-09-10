from rest_framework.generics import ListCreateAPIView

from apps.common.models import SubEmail
from .serializers import SubEmailLCSerializer


class SubEmailLCView(ListCreateAPIView):
    """
    View for listing and creating subemails.
    """

    queryset = SubEmail.objects.all()
    serializer_class = SubEmailLCSerializer
    pagination_class = None

    def get_queryset(self):
        return SubEmail.objects.filter(is_active=True)
