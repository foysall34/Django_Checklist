from django.urls import path
from .views import GoogleAuthView

urlpatterns = [
    path('api/google-login/', GoogleAuthView.as_view(), name='google-login')
]