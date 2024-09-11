from django.urls  import path

from .api.content.ContentRetrieve.views import ContentRetrieveView


app_name = 'youtube'

urlpatterns = [
    path('content_retrieve/<slug:slug>/', ContentRetrieveView.as_view(), name='content_retrieve'),
]
