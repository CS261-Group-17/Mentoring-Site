from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from app.models import *
from app.serializers import *


############
### User ###
############

@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_profile_list(request):
    """
    get:
        Get the list of all user profiles.
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def user_register(request):
    """
    post:
        Register a user.
    """
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid() and 'password' in request.data:
        user = serialized.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    get:
        Get the contents of the user's profile.

    patch:
        Update the contents of the user's profile.
    """
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    elif request.method == 'PATCH':
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def user_email(request):
    """
    get:
        Return the user's email.

    patch:
        Update the user's email.
    """
    if request.method == 'GET':
        serializer = EmailSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    else:
        serializer = EmailSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def user_password(request):
    """
    patch:
        Update the user's password.
    """
    if 'password' in request.data:
        serialized = UserSerializer(data=request.user)
        user = serialized.save()
        user.set_password(request.data.get('password'))
        user.save()
    else:
        return Response("No new password provided", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    """
    delete:
        Delete a user account.
    """
    try:
        user = User.objects.get(username__exact=request.user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    user.delete()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """
    get:
        Log out a user.
    """
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)



##############
### Topics ###
##############

@api_view(['GET', 'POST', 'DELETE'])
def topics(request):
    """
    get:
        Get the list of all topics of strengths/weaknesses.

    post:
        Add a topic of strengths/weaknesses.

    delete:
        Delete a topic of strengths/weaknesses.
    """
    if request.method == 'GET':
        strength_weaknesses = StrengthWeakness.objects.all()
        serializer = StrengthWeaknessSerializer(strength_weaknesses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # TODO: Add a note of who added it
        serializer = StrengthWeaknessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'sw_type' in request.data:
        topics = StrengthWeakness.objects.filter(sw_type__exact=request.data.get('sw_type'))
        serialized = None
        for topic in topics:
            serialized = StrengthWeaknessSerializer(topic)
            topic.delete()
        if serialized is not None:
            return Response(serialized.data, status=status.HTTP_202_ACCEPTED)
        return Response("Cannot delete non-existent topic", status=status.HTTP_400_BAD_REQUEST)
