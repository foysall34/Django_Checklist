from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from .permission import IsOwner
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 




@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_create_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializers = PostSerializer(post , many = True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = PostSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_200_OK)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method in ['PUT', 'DELETE']:
        owner_check = IsOwner()
        if not owner_check.has_object_permission(request, None, post):
            return Response(
                {"detail": "You don't have permission to change it"},
                status=status.HTTP_403_FORBIDDEN
            )

    if request.method == 'GET':
        serializers = PostSerializer(post)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = PostSerializer(post, data=request.data)
        if serializers.is_valid():
            serializers.save(owner=post.owner)
            return Response(serializers.data)
        return Response(serializers.errors)

    elif request.method == 'DELETE':
        post.delete()
        return Response({"msg" : "data deleted"},status=status.HTTP_204_NO_CONTENT  )
        

# For decorators 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .decorators import email_domain_required

@api_view(['GET'])
@email_domain_required(domain='.com')
def protected_view(request):
    return Response({"message": "You have access because your email ends with @gmail.com"})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import pytz

@api_view(['GET'])
def current_time_view(request):
    bangladesh_time = datetime.now(pytz.timezone('Asia/Dhaka'))
    
    return Response({
        "current_time": bangladesh_time.strftime("%Y-%m-%d %H:%M:%S"),  # includes seconds
        "timezone": "Asia/Dhaka"
    })
