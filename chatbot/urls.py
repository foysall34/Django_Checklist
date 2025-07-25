from django.urls import path
from .views import ChatBotAPIView , ChatAPIViewIntermidiate

urlpatterns = [
    path('chat/', ChatBotAPIView.as_view(), name='chat-api'),
    path('chats/', ChatAPIViewIntermidiate.as_view(), name='chat'),
]
