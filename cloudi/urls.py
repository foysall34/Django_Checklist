from django.urls import path
from .views import  media_item_list_create,detect_food

urlpatterns = [
   path('media-items/', media_item_list_create, name='media-items'),
   path('detect-food/', detect_food, name='detect-food'),
 
   
   ]
