from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import *

# https://www.geeksforgeeks.org/function-based-views-django-rest-framework/

#####################
### USER ACCOUNTS ###
#####################


@api_view(['GET'])
def user_profile_list(request):
    """List the profile data of all the users"""
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register(request):
    """Register a new user"""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # When we do authentication, this should also return an auth token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST']) # This could be a PATCH type?
def user_profile(request, email):
    """Get the profile of a user specified by their email address"""
    try:
        user = User.objects.get(email__exact=email)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############################
### STRENGTHS WEAKNESSES ###
############################
@api_view(['GET', 'POST'])
def strength_weaknesses(request):
    if request.method == 'GET':
        strength_weaknesses = StrengthWeakness.objects.all()
        serializer = StrengthWeaknessSerializer(strength_weaknesses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StrengthWeaknessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # When we do authentication, this should also return an auth token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
