from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
