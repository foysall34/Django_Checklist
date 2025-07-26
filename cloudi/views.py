# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer
import cloudinary.uploader
from .serializers import FoodImageSerializer , APIUserSerializer
import requests
from django.conf import settings 
from rest_framework.views import APIView
from .models import APIUser
from rest_framework.permissions import IsAuthenticated

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
    
# for 3rd party api intregation (LogMeal)

LOGMEAL_API_KEY = settings.LOGMEAL_API_KEY

@api_view(['POST'])
def detect_food(request):
    serializer = FoodImageSerializer(data=request.data)
    if serializer.is_valid():
        image = serializer.validated_data['image']

        # LogMeal এ image পাঠাতে হবে file format এ
        files = {'image': image}
        headers = {'Authorization': f'Bearer {LOGMEAL_API_KEY}'}

        try:
            res = requests.post(
                'https://api.logmeal.es/v2/image/recognition/complete',
                files=files,
                headers=headers
            )
            return Response(res.json(), status=res.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    return Response(serializer.errors, status=400)




# for logMeal
import uuid

class APIUserCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        if APIUser.objects.filter(user=user).count() >= 5:
            return Response({'error': 'You can only register up to 3 API users.'}, status=400)

        data = request.data.copy()
        data['user'] = user.id
        data['token'] = str(uuid.uuid4())[:16]  

        serializer = APIUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
