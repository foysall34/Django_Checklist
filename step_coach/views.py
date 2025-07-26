from .models import Addiction ,UserProfile
from .serializers import AddictionSerializer, SelectAddictionSerializer

from rest_framework import generics,permissions

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.

class AddictionListView(generics.ListAPIView):
    serializer_class = AddictionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('search')
        if query:
            return Addiction.objects.filter(name__icontains=query)
        return Addiction.objects.all()

class SelectAddictionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SelectAddictionSerializer(data=request.data)
        if serializer.is_valid():
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            serializer.save(user_profile=profile)
            return Response({"message": "Addictions set successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
