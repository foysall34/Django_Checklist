from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from .utils import get_bot_reply

# Basic level chatboot 
class ChatBotAPIView(APIView):
    def post(self, request):
        message = request.data.get('message', '').lower()

        if 'hello' in message or 'hi' in message:
            reply = "Hello! How can I help you?"
        elif 'how are you ?' in message:
            reply= "I'm doing well, what about you ?"
        elif 'price' in message:
            reply = "Our products start from 500 BDT."
        elif 'thanks' in message:
            reply = "You're welcome!"
        else:
            reply = "Sorry, I didn’t understand that."

        return Response({"reply": reply}, status=status.HTTP_200_OK)



# Intermidiate level chat bot 
class ChatAPIViewIntermidiate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        message = request.data.get("message")

        if not message:
            return Response({"error": "Message is required"}, status=400)

        reply = get_bot_reply(message)

        chat = ChatMessage.objects.create(user=user, message=message, reply=reply)
        serializer = ChatMessageSerializer(chat)
        return Response(serializer.data, status=201)

    def get(self, request):
        # Return chat history of the user
        messages = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data)
