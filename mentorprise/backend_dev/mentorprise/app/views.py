from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from app.models import *
from app.serializers import *


############
### User ###
############

@api_view(['GET'])                  # TODO: THIS SHOULD NOT BE IN PRODUCTION!
def user_profile_list(request):
    """
    An API endpoint over all user profiles
        - GET:      Get the list of all user profiles
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    An API endpoint for a specific user's profile
        - GET:      Get the contents of the user's profile
        - PATCH:    Update the contents of the user's profile
    """
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_register(request):
    """
    An API endpoint to register a user account
        - POST:     Register a user
    """
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def user_delete(request):
    """
    An API endpoint to delete a specific user's account
        - DELETE:     Delete a user account
    """
    if request.method == 'DELETE':
        try:
            user = User.objects.get(username__exact=request.user)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        user.delete()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def user_logout(request):
    """
    An API endpoint to log out a user
        - POST:     Log out a user
    """
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
