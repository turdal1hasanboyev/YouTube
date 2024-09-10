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
]
