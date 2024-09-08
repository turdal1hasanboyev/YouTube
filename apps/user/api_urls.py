from django.urls import path

from .api.user.UserLC.views import UserLCView
from .api.user.UserRUD.views import UserRUDView

from .api.friendrequest.FriendRequestCreate.views import FriendRequestCreateView
from .api.friendrequest.FriendRequestList.views import FriendRequestListView
from .api.friendrequest.FriendRequestDestroy.views import FriendRequestDestroyView
from .api.friendrequest.FriendRequestRetrieve.views import FriendRequestRetrieveView
from .api.friendrequest.FriendRequestUpdate.views import FriendRequestUpdateView


app_name = 'user'

urlpatterns = [
    path('user_lc/', UserLCView.as_view(), name='user_lc'),
    path('user_rud/<int:pk>/', UserRUDView.as_view(), name='user_rud'),

    path('friend_request_create/', FriendRequestCreateView.as_view(), name='friend_request_create'),
    path('friend_request_list/', FriendRequestListView.as_view(), name='friend_request_list'),
    path('friend_request_destroy/<int:pk>/', FriendRequestDestroyView.as_view(), name='friend_request_destroy'),
    path('friend_request_retrieve/<int:pk>/', FriendRequestRetrieveView.as_view(), name='friend_request_retrieve'),
    path('friend_request_update/<int:pk>/', FriendRequestUpdateView.as_view(), name='friend_request_update'),
]
