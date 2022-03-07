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
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid() and 'password' in request.data:
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

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
    elif request.method == 'PATCH':
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
        serializer = UserSerializer(data=request.user)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
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
@permission_classes([IsAuthenticated])
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
        serializer = None
        for topic in topics:
            serializer = StrengthWeaknessSerializer(topic)
            topic.delete()
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response("Cannot delete non-existent topic", status=status.HTTP_400_BAD_REQUEST)

#####################
### Notifications ###
#####################

@api_view(['GET', 'PATCH', 'POST']) # TODO: REMOVE POST, ONLY FOR DEBUGGING! 
@permission_classes([IsAuthenticated])
def notifications_list(request):
    """
    get:
        Return the list of all the user's notifications.
    patch:
        Set a specific notification to be read.
    """
    if request.method == 'GET':
        notifications = Notification.objects.all().filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        return Response("API not yet implemented", status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Create a new notification with request.user as the user field, and
        # request.data populating all other fields
        serializer = NotificationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################
### Feedback ###
################

# @api_view(['GET', 'POST', 'PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def feedback_meeting(request):
#     """
#     get:
#         Get the contents of the meeting feedback.
#     post:
#         Add a new meeting feedback from a user.
#     patch:
#         Modify the meeting feedback from a user.
#     delete:
#         Delete a the user's meeting feedback.
#     """
#     # if 'meeting' in request.data:
#     #     if request.method == 'GET':
#     #         pass
#     #     elif request.method == 'POST':
#     #         pass
#     #     elif request.method == 'PATCH':
#     #         pass
#     #     elif request.method == 'DELETE':
#     #         pass
#     # return Response("No meeting provided", status=status.HTTP_400_BAD_REQUEST)
#     return Response("API not yet implemented", status=status.HTTP_200_OK)


# @api_view(['GET', 'PATCH'])
# @permission_classes([IsAuthenticated])
# def feedback_mentor(request):
#     """
#     get:
#         Get the contents of the mentor feedback.
#     patch:
#         Modify the mentor feedback from a user.
#     """
#     return Response("API not yet implemented", status=status.HTTP_200_OK)

# @api_view(['GET', 'POST', 'DELETE'])
# # @permission_classes([IsAuthenticated])
# def feedback_system(request):
#     """
#     get:
#         Get the contents of the system feedback.
#     post:
#         Add a new system feedback from a user.
#     delete:
#         Delete a the user's system feedback.
#     """
#     if request.method == 'GET':
#         feedback = SystemFeedback.objects.all() #.filter(user=request.user)
#         serializer = SystemFeedbackSerializer(feedback, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StrengthWeaknessSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response("API not yet implemented", status=status.HTTP_200_OK)
