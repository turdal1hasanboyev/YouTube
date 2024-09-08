from django.urls import path

from .api.user.UserLC.views import UserLCView
from .api.user.UserRUD.views import UserRUDView

from .api.friendrequest.FriendRequestLC.views import FriendRequestLCView
from .api.friendrequest.FriendRequestRUD.views import FriendRequestRUDView


app_name = 'user'

urlpatterns = [
    path('user_lc/', UserLCView.as_view(), name='user_lc'),
    path('user_rud/<int:pk>', UserRUDView.as_view(), name='user_rud'),

    path('friend_request_lc/', FriendRequestLCView.as_view(), name='friend_request_lc'),
    path('friend_request_rud/<int:pk>', FriendRequestRUDView.as_view(), name='friend_request_rud'),
]
