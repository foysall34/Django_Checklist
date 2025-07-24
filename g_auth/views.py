from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
import requests

class GoogleAuthView(APIView):
    def post(self, request):
        token_id = request.data.get("token")

        # Verify with Google
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token_id}")
        if response.status_code != 200:
            return Response({"error": "Invalid token"}, status=400)

        data = response.json()
        email = data["email"]

        user, created = User.objects.get_or_create(email=email, defaults={
            "username": email,
            "first_name": data.get("given_name", "")
        })

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })
