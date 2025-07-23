from django.urls import path
from .views import  media_item_list_create

urlpatterns = [
   path('media-items/', media_item_list_create, name='media-items'),
]
