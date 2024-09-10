from django.urls  import path

from .api.category.CategoryLC.views import CategoryLCView
from .api.category.CategoryRUD.views import CategoryRUDView

from .api.tag.TagLC.views import TagLCView
from .api.tag.TagRUD.views import TagRUDView


app_name = 'common'

urlpatterns = [
    path('category_lc/', CategoryLCView.as_view(), name='category_lc'),
    path('category_rud/<slug:slug>/', CategoryRUDView.as_view(), name='category_rud'),
    
    path('tag_lc/', TagLCView.as_view(), name='tag_lc'),
    path('tag_rud/<slug:slug>/', TagRUDView.as_view(), name='tag_rud'),
]
