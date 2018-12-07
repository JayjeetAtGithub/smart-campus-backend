<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .models import User

""" Follow the below coded style of making api endpoints
"""


@api_view(['GET'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def get_all_users(request, format=None):
    """Fetches the details of all users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def get_user(request, username, format=None):
    """Fetches the details of the user whose username is passed through the url.
    """
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
=======
from django.shortcuts import render
from django.contrib.auth import get_user_model

#Django sucks here, Need to import the custom User model explicitly, default is auth.User
User = get_user_model()
>>>>>>> f1590b6c9684816d6f5d26fe5e5e46f042504245

