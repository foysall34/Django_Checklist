from django.urls import path
from .views import post_create_list, post_details, protected_view, current_time_view

urlpatterns = [
    path('posts/', post_create_list, name='post-list-create'),
    path('posts/<int:pk>/', post_details, name='post-detail'),
    path('protected/', protected_view, name='protected-view'),
    path('time/', current_time_view, name='current-time'),
]
