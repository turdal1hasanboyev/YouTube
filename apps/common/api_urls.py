from django.urls  import path

from .api.category.CategoryLC.views import CategoryLCView
from .api.category.CategoryRUD.views import CategoryRUDView

from .api.tag.TagLC.views import TagLCView
from .api.tag.TagRUD.views import TagRUDView

from .api.country.CountryLC.views import CountryLCView
from .api.country.CountryRUD.views import CountryRUDView

from .api.playlist.PlayListLC.views import PlayListLCView
from .api.playlist.PlayListRUD.views import PlayListRUDView

from .api.subemail.SubEmailLC.views import SubEmailLCView
from .api.subemail.SubEmailRUD.views import SubEmailRUDView

from .api.channel.ChannelCreate.views import ChannelCreateView
from .api.channel.ChannelRetrieve.views import ChannelRetrieveView
from .api.channel.ChannelList.views import ChannelListView
from .api.channel.ChannelUpdate.views import ChannelUpdateView
from .api.channel.ChannelDestroy.views import ChannelDestroyView

from .api.subscription.SubscriptionCreate.views import SubscriptionCreateView
from .api.subscription.SubscriptionList.views import SubscriptionListView
from .api.subscription.SubscriptionDestroy.views import SubscriptionDestroyView
from .api.subscription.SubscriptionRetrieve.views import SubscriptionRetrieveView
from .api.subscription.SubscriptionUpdate.views import SubscriptionUpdateView

from .api.contact.ContactCreate.views import ContactCreateView
from .api.contact.ContactList.views import ContactListView
from .api.contact.ContactUpdate.views import ContactUpdateView
from .api.contact.ContactRetrieve.views import ContactRetrieveView
from .api.contact.ContactDestroy.views import ContactDestroyView


app_name = 'common'

urlpatterns = [
    path('category_lc/', CategoryLCView.as_view(), name='category_lc'),
    path('category_rud/<slug:slug>/', CategoryRUDView.as_view(), name='category_rud'),
    
    path('tag_lc/', TagLCView.as_view(), name='tag_lc'),
    path('tag_rud/<slug:slug>/', TagRUDView.as_view(), name='tag_rud'),

    path('country_lc/', CountryLCView.as_view(), name='country_lc'),
    path('country_rud/<slug:slug>/', CountryRUDView.as_view(), name='country_rud'),

    path('play_list_lc/', PlayListLCView.as_view(), name='play_list_lc'),
    path('play_list_rud/<slug:slug>/', PlayListRUDView.as_view(), name='play_list_rud'),

    path('sub_email_lc/', SubEmailLCView.as_view(), name='sub_email_lc'),
    path('sub_email_rud/<int:pk>/', SubEmailRUDView.as_view(), name='sub_email_rud'),

    path('channel_create/', ChannelCreateView.as_view(), name='channel_create'),
    path('channel_retrieve/<slug:slug>/', ChannelRetrieveView.as_view(), name='channel_retrieve'),
    path('channel_list/', ChannelListView.as_view(), name="channel_list"),
    path('channel_update/<slug:slug>/', ChannelUpdateView.as_view(), name='channel_update'),
    path('channel_destroy/<slug:slug>/', ChannelDestroyView.as_view(), name='channel_destroy'),

    path('subscription_create/', SubscriptionCreateView.as_view(), name='subscription_create'),
    path('subscription_list/', SubscriptionListView.as_view(), name='subscription_list'),
    path('subscription_destroy/<int:pk>/', SubscriptionDestroyView.as_view(), name='subscription_destroy'),
    path('subscription_retrieve/<int:pk>/', SubscriptionRetrieveView.as_view(), name='subscription_retrieve'),
    path('subscription_update/<int:pk>/', SubscriptionUpdateView.as_view(), name='subscription_update'),

    path('contact_create/', ContactCreateView.as_view(), name='contact_create'),
    path('contact_list/', ContactListView.as_view(), name='contact_list'),
    path('contact_update/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('contact_retrieve/<int:pk>/', ContactRetrieveView.as_view(), name='contact_retrieve'),
    path('contact_destroy/<int:pk>/', ContactDestroyView.as_view(), name='contact_destroy'),
]
