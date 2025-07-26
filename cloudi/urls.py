from django.urls import path
from .views import  media_item_list_create,detect_food, APIUserCreateView

urlpatterns = [
   path('media-items/', media_item_list_create, name='media-items'),
   path('detect-food/', detect_food, name='detect-food'),
    path('create-api-user/', APIUserCreateView.as_view(), name='create_api_user'),
 
   
   ]
