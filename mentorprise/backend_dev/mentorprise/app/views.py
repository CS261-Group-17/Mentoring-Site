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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_list(request):
    """
    An API endpoint over all user profiles
        - GET:      Get the list of all user profiles
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def user_register(request):
    # TODO: Need to put this in a try block
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = serialized.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['POST'])
def user_logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
