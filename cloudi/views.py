# myapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer

@api_view(['GET', 'POST'])
def media_item_list_create(request):
    if request.method == 'GET':
        items = MediaItem.objects.all()
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MediaItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
