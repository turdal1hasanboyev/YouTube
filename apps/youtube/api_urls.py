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

from .api.comment.CommentRetrieve.views import CommentRetrieveView
from .api.comment.CommentList.views import CommentListView
from .api.comment.CommentCreate.views import CommentCreateView
from .api.comment.CommentDestroy.views import CommentDestroyView
from .api.comment.CommentUpdate.views import CommentUpdateView

from .api.savedforlater.SavedForLaterCreate.views import SavedForLaterCreateView
from .api.savedforlater.SavedForLaterList.views import SavedForLaterListView
from .api.savedforlater.SavedForLaterDestroy.views import SavedForLaterDestroyView
from .api.savedforlater.SavedForLaterRetrieve.views import SavedForLaterRetrieveView
from .api.savedforlater.SavedForLaterUpdate.views import SavedForLaterUpdateView

from .api.premiera.PremieraCreate.views import PremieraCreateView
from .api.premiera.PremieraList.views import PremieraListView
from .api.premiera.PremieraDestroy.views import PremieraDestroyView
from .api.premiera.PremieraRetrieve.views import PremieraRetrieveView
from .api.premiera.PremieraUpdate.views import PremieraUpdateView


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

    path('comment_retrieve/<int:pk>/', CommentRetrieveView.as_view(), name='comment_retrieve'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
    path('comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment_destroy/<int:pk>/', CommentDestroyView.as_view(), name='comment_destroy'),
    path('comment_update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),

    path('saved_for_later_create/', SavedForLaterCreateView.as_view(), name='saved_for_later_create'),
    path('saved_for_later_list/', SavedForLaterListView.as_view(), name='saved_for_later_list'),
    path('saved_for_later_destroy/<int:pk>/', SavedForLaterDestroyView.as_view(), name='saved_for_later_destroy'),
    path('saved_for_later_retrieve/<int:pk>/', SavedForLaterRetrieveView.as_view(), name='saved_for_later_retrieve'),
    path('saved_for_later_update/<int:pk>/', SavedForLaterUpdateView.as_view(), name='saved_for_later_update'),

    path('premiere_create/', PremieraCreateView.as_view(), name='premiere_create'),
    path('premiere_list/', PremieraListView.as_view(), name='premiere_list'),
    path('premiere_destroy/<int:pk>/', PremieraDestroyView.as_view(), name='premiere_destroy'),
    path('premiere_retrieve/<int:pk>/', PremieraRetrieveView.as_view(), name='premiere_retrieve'),
    path('premiere_update/<int:pk>/', PremieraUpdateView.as_view(), name='premiere_update'),
]
