# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer
import cloudinary.uploader

@api_view(['GET', 'POST'])
def media_item_list_create(request):
    if request.method == 'GET':
        items = MediaItem.objects.all()
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        video_file = request.FILES.get('video')
        document_file = request.FILES.get('document')

        video_url = None
        document_url = None

        #  Upload video if provided
        if video_file:
            try:
                upload_result = cloudinary.uploader.upload(
                    video_file,
                    resource_type='video'
                )
                video_url = upload_result['secure_url']
            except Exception as e:
                return Response({'error': f'Video upload failed: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        #  Upload document if provided
        if document_file:
            try:
                upload_result = cloudinary.uploader.upload(
                    document_file,
                    resource_type='raw'
                )
                document_url = upload_result['secure_url']
            except Exception as e:
                return Response({'error': f'Document upload failed: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        if not video_url and not document_url:
            return Response({'error': 'No video or document file provided'}, status=status.HTTP_400_BAD_REQUEST)

        #  Save to DB
        media_item = MediaItem.objects.create(
            title=title,
            video=video_url,
            document=document_url
        )
        serializer = MediaItemSerializer(media_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)