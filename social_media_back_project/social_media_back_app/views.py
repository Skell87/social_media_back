from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
        try:
              username = request.data.get('username')
              password = request.data.get('password')

              user = User.objects.create(
                    username=username
              )
              user.set_password(password)
              user.save()

              profile = Profile.objects.create(
                    user=user,    
                    first_name = request.data.get('firstName', ''),
                    last_name = request.data.get('lastName', '')
              )
              profile.save()
              profile_serialized = ProfileSerializer(profile)
              return Response(profile_serialized.data, status=status.HTTP_201_CREATED)
        except Exception as e:
              return Response({'error': str(e)}, status=400)
        
@api_view(['POST', 'GET'])
@permission_classes([])
def user_post(request):
      if request.method == 'GET':
            posts = UserPost.objects.all()
            serializer = UserPostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
      
      if request.method == 'POST':
      
            try:
                  # this gets the content we supplied from the front
                  content = request.data['content']
                  if not content:
                        return Response({'error': 'content required'}, status=status.HTTP_400_BAD_REQUEST)

                  # this creates a new UserPost instance,
                  # creating it with the requested user information and the content.
                  # setting the created content = to the supplied content.
                  user_post = UserPost.objects.create(
                        user=request.user,
                        content=content
                  )

                  # serializes the newly created post
                  serializer = UserPostSerializer(user_post)

                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                  return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_posts(request):
      if request.method == 'GET':
            user = request.user
            posts = UserPost.objects.filter(user=user)
            serializer = UserPostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_post(request):
      if request.method == 'POST':
            post_id = request.data.get('post_id')
            try:
                  post = UserPost.objects.get(id=post_id, user=request.user)
                  post.delete()
                  return Response(status=status.HTTP_204_NO_CONTENT)
            except UserPost.DoesNotExist:
                  return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                  return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
