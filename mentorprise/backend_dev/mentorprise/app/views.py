from curses import meta
from functools import partial
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
@permission_classes([IsAuthenticated]) # @permission_classes([IsAdminUser])
def user_profile_list(request):
    """
    get:
        Get the list of all user profiles.
    """
    user = User.objects.all().order_by('-first_name')
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = UserProfileSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
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
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
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

#################
### Mentoring ###
#################


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mentoring_mentees_list(request):
    """
    get:
        Get the list of all the user's mentees.
    """
    pairings = Pairing.objects.filter(mentor=request.user.id).filter(
                terminated=False).filter(in_proposal=False)
    mentee_ids = pairings.values_list('mentee', flat=True)
    mentees = User.objects.filter(id__in=mentee_ids)
    serializer = UserSerializer(mentees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def mentoring_mentee(request):
    """
    get:
        Get the profile of the mentee.
    delete:
        Terminate the relationship with the mentee.
    """
    if 'mentee' in request.data:
        try:
            pairings = Pairing.objects.filter(mentor=request.user).filter(
                terminated=False).filter(in_proposal=False)
            mentee = User.objects.get(username__exact=request.data.get('mentee'))
            pairing = pairings.get(mentee=mentee.id)
            if request.method == 'GET':
                serializer = UserSerializer(pairing.mentee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'DELETE':
                # TODO: I do not know how to do this :kekw:
                serializer = PairingSerializer(pairing, data={"terminated": True}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pairing.DoesNotExist:
            return Response("Pairing does not exist", status=status.HTTP_404_NOT_FOUND)
    return Response("No mentee provided", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def mentoring_mentor(request):
    """
    get:
        Get the profile of the mentor
    delete:
        Terminate the relationship with the mentor
    """
    try:
        pairing = Pairing.objects.filter(mentee=request.user).filter(
            terminated=False).filter(in_proposal=False).first()
        if request.method == 'GET':
            serializer = UserSerializer(pairing.mentor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            # TODO: I do not know how to do this :kekw:
            serializer = PairingSerializer(pairing, data={"terminated": True}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response("No mentor exists", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def mentoring_proposed_mentors(request):
    """
    get:
        Get the list of mentors offering mentorship
    post:
        Accept a mentor's offer of mentoring
    delete:
        Decline a mentor's offer of mentoring
    """
    if request.method == 'GET':
        pairings = Pairing.objects.filter(mentee=request.user.id).filter(
                    terminated=False).filter(in_proposal=True)
        mentor_ids = pairings.values_list('mentor', flat=True)
        mentors = User.objects.filter(id__in=mentor_ids)
        serializer = UserSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif 'mentor' in request.data:
        pairings = Pairing.objects.filter(mentee=request.user).filter(
            terminated=False).filter(in_proposal=True)
        mentor = User.objects.get(username=request.data.get('mentor'))
        pairing = pairings.get(mentor=mentor)                                   # TODO: Add error handling on all .gets()
        if request.method == 'POST':
            serializer = PairingSerializer(pairing, data={"in_proposal": False}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        elif request.method == 'DELETE':
            # TODO: I do not know how to do this :kekw:
            serializer = PairingSerializer(data={"terminated": True}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mentoring_potential_mentees_list(request):
    """
    get:
        Get the ordered list of possible mentees
    post:
        Offer mentorship to a mentee
    """
    if request.method == 'GET':
        # TODO: This is our mentor matching bit
        possible_mentees = User.objects.order_by('-first_name')
        serializer = UserSerializer(possible_mentees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if 'mentee' in request.data:
            try:
                mentee = User.objects.get(username__exact=request.data.get('mentee'))
                serializer = PairingSerializer(data={
                    "mentee": mentee.id,
                    "mentor": request.user.id,
                    "in_proposal": True,
                    "terminated": False
                })
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        return Response("No mentee provided", status=status.HTTP_400_BAD_REQUEST)
















##############
### Topics ###
##############

@api_view(['GET', 'POST', 'DELETE'])  # TODO: Add a note of who added it
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StrengthWeaknessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'sw_type' in request.data:
        topics = StrengthWeakness.objects.filter(
            sw_type__exact=request.data.get('sw_type'))
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


@api_view(['GET', 'PATCH', 'POST'])  # TODO: REMOVE POST, ONLY FOR DEBUGGING!
@permission_classes([IsAuthenticated])
def notifications_list(request):
    """
    get:
        Return the list of all the user's notifications.
    patch:
        Set a specific notification to be read.
    """
    if request.method == 'GET':
        notifications = Notification.objects.filter(user__exact=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        return Response("API not yet implemented", status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NotificationSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################
### Feedback ###
################

@api_view(['GET', 'POST'])  # TODO: Make get viewable only by an admin
def feedback_system(request):
    """
    get:
        Get the contents of the system feedback.
    post:
        Add a new system feedback from a user.
    delete:
        Delete a the user's system feedback.
    """
    if request.method == 'GET':
        feedback = SystemFeedback.objects.all()
        serializer = SystemFeedbackSerializer(feedback, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SystemFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("API not yet implemented", status=status.HTTP_200_OK)

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
#     """
#     if 'meeting' in request.data:
#         try:
#             meeting = Meeting.objects.get(id__exact=request.data.get('meeting'))
#             if request.method == 'GET':
#                 serializer = SystemFeedbackSerializer(meeting)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             elif request.method == 'POST':
#                 serializer = MeetingFeedbackSerializer(
#                     data=request.data,
#                     context={'request': request, 'meeting': meeting}
#                 )
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             elif request.method == 'PATCH':
#                 serializer = MeetingFeedbackSerializer(
#                     data=request.data,
#                     context={'request': request, 'meeting': meeting},
#                     partial=True    # TODO: Same as POST other than this. Can merge?
#                 )
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Meeting.DoesNotExist:
#             return Response("Meeting does not exist", status=status.HTTP_404_NOT_FOUND)
#     return Response("No meeting provided", status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PATCH'])     # TODO: Does this need to be somehow initialised empty?
# @permission_classes([IsAuthenticated])
# def feedback_mentor(request):
#     """
#     get:
#         Get the contents of the mentor feedback.
#     patch:
#         Modify the mentor feedback from a user.
#     """
#     return Response("API not yet implemented", status=status.HTTP_200_OK)

####################
### Group events ###
####################

#######################
### Plans of action ###
#######################

################
### Meetings ###
################
