from django.urls  import path

from .api.content.ContentRetrieve.views import ContentRetrieveView
from .api.content.ContentList.views import ContentListView
from .api.content.ContentCreate.views import ContentCreateView
from .api.content.ContentUpdate.views import ContentUpdateView
from .api.content.ContentDestroy.views import ContentDestroyView

from .api.liked.LikedRetrieve.views import LikedRetrieveView
from .api.liked.LikedList.views import LikedListView
from .api.liked.LikedDestroy.views import LikedDestroyView
from .api.liked.LikedCreate.views import LikedCreateView
from .api.liked.LikedUpdate.views import LikedUpdateView


app_name = 'youtube'

urlpatterns = [
    path('content_retrieve/<slug:slug>/', ContentRetrieveView.as_view(), name='content_retrieve'),
    path('content_list/', ContentListView.as_view(), name='content_list'),
    path('content_create/', ContentCreateView.as_view(), name='content_create'),
    path('content_update/<slug:slug>/', ContentUpdateView.as_view(), name='content_update'),
    path('content_destroy/<slug:slug>/', ContentDestroyView.as_view(), name='content_destroy'),
    
    path('liked_retrieve/<int:pk>/', LikedRetrieveView.as_view(), name='liked_retrieve'),
    path('liked_list/', LikedListView.as_view(), name='liked_list'),
    path('liked_destroy/<int:pk>/', LikedDestroyView.as_view(), name='liked_destroy'),
    path('liked_create/', LikedCreateView.as_view(), name='liked_create'),
    path('liked_update/<int:pk>/', LikedUpdateView.as_view(), name='liked_update'),
]
