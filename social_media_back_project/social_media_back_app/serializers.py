from rest_framework import serializers
from .models import *
from datetime import datetime
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name']

class UserPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    date_created = serializers.DateTimeField('%A, %d. %B %Y %I:%M%p')
    # new_date_created = date_created.datetime.strftime('%A, %d. %B %Y %I:%M%p')
    class Meta:
    
        model = UserPost
        fields = ['id', 'user', 'content', 'date_created']