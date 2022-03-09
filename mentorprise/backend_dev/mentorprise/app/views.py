from django.db.models import Q
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
# @permission_classes([IsAdminUser])
def user_profile_list(request):
    """
    get:
        Get the list of all user profiles.
    """
    # Get all the user objects ordered by name
    user = User.objects.all().order_by('-first_name')
    # Serialize and return all the user objects
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_register(request):
    """
    post:
        Register a user.
    """
    # Serialize the provided user data
    serializer = UserSerializer(data=request.data)
    # If the provided data is valid, and a password is provided, save the user
    # data into a new object, and update its password
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
        # Get the profile of the user who sent the request
        serializer = UserProfileSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    elif request.method == 'PATCH':
        # Try to update the profile of the user who sent the request with the
        # data in the request
        serializer = UserProfileSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def user_account(request):
    """
    get:
        Return the user's account.
    patch:
        Update the user's account.
    """
    if request.method == 'GET':
        # Get the account of the user who sent the request
        serializer = AccountSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    elif request.method == 'PATCH':
        # Try to update the account of the user who sent the request
        serializer = AccountSerializer(
            request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_strengths(request):
    """
    get:
        Get all the user's strengths
    post:
        Add a user strength
    delete:
        Delete a user strength
    """
    if request.method == 'GET':
        # Serialize then return all the user's strengths
        strengths_weaknesses = StrengthList.objects.filter(user=request.user)
        # Get a list of ids for the sw_types in these pairings
        sw_type_ids = strengths_weaknesses.values_list('sw_type', flat=True)
        # Get a list of users who are sw_types of the user who sent the request,
        # then serialize them and return them
        sw_types = StrengthWeakness.objects.filter(id__in=sw_type_ids)
        serializer = StrengthWeaknessSerializer(sw_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST' and 'sw_type' in request.data:
        try:
            # Get the strength with the name
            strength = StrengthWeakness.objects.get(
                sw_type__exact=request.data.get('sw_type'))
            # Add the user as having that strength
            serializer = StrengthListSerializer(
                data=request.data, context={'request': request, 'sw_type': strength})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StrengthList.DoesNotExist:
            return Response("Cannot add non-existent strength", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'sw_type' in request.data:
        try:
            # Get the strength with the name
            strength = StrengthWeakness.objects.get(
                sw_type__exact=request.data.get('sw_type'))
            user_strength = StrengthList.objects.filter(
                user=request.user).get(sw_type=strength)
            serializer = StrengthListSerializer(user_strength)
            user_strength.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except StrengthList.DoesNotExist:
            return Response("Cannot delete non-existent strength", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_weaknesses(request):
    """
    get:
        Get all the user's weaknesses
    post:
        Add a user weakness
    delete:
        Delete a user weakness
    """
    if request.method == 'GET':
        # Serialize then return all the user's strengths
        strengths_weaknesses = WeaknessList.objects.filter(user=request.user)
        # Get a list of ids for the sw_types in these pairings
        sw_type_ids = strengths_weaknesses.values_list('sw_type', flat=True)
        # Get a list of users who are sw_types of the user who sent the request,
        # then serialize them and return them
        sw_types = StrengthWeakness.objects.filter(id__in=sw_type_ids)
        serializer = StrengthWeaknessSerializer(sw_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST' and 'sw_type' in request.data:
        try:
            # Get the weakness with the name
            weakness = StrengthWeakness.objects.get(
                sw_type__exact=request.data.get('sw_type'))
            # Add the user as having that weakness
            serializer = WeaknessListSerializer(
                data=request.data, context={'request': request, 'sw_type': weakness})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WeaknessList.DoesNotExist:
            return Response("Cannot add non-existent weakness", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'sw_type' in request.data:
        try:
            # Get the weakness with the name
            weakness = StrengthWeakness.objects.get(
                sw_type__exact=request.data.get('sw_type'))
            user_weakness = WeaknessList.objects.filter(
                user=request.user).get(sw_type=weakness)
            serializer = WeaknessListSerializer(user_weakness)
            user_weakness.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except WeaknessList.DoesNotExist:
            return Response("Cannot delete non-existent weakness", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def user_password(request):
    """
    patch:
        Update the user's password.
    """
    # Try to update the password of the user who sent the request
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
    # Delete the user who sent the request
    serializer = UserSerializer(request.user)
    request.user.delete()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """
    get:
        Log out a user.
    """
    # Revoke the token for the user who sent the request, logging them out
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
    # Get the pairings with the mentees of the user who sent the request by
    # filtering over all pairings for the one who made the request, then
    # excluding terminated and unapproved relationships
    pairings = Pairing.objects.filter(mentor=request.user.id).filter(   # TODO: Omit user.id
        terminated=False).filter(in_proposal=False)
    # Get a list of ids for the mentees in these pairings
    mentee_ids = pairings.values_list('mentee', flat=True)
    # Get a list of users who are mentees of the user who sent the request,
    # then serialize them and return them
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
            # Get the current pairings for which the user who sent the request
            # is the mentor
            pairings = Pairing.objects.filter(mentor=request.user).filter(
                terminated=False).filter(in_proposal=False)
            # Get the user object for the mentee with the specified username
            mentee = User.objects.get(
                username__exact=request.data.get('mentee'))
            # From the requesting users pairings, get the pairing with the
            # requested mentee
            pairing = pairings.get(mentee=mentee.id)
            if request.method == 'GET':
                # Serialize then return the mentee
                serializer = UserSerializer(pairing.mentee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'DELETE':
                # Update the pairing to be terminated through its serializer
                serializer = PairingSerializer(
                    pairing, data={"terminated": True}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, Pairing.DoesNotExist):
            return Response("Mentee or pairing does not exist", status=status.HTTP_404_NOT_FOUND)
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
        # Get the current pairings for which the user who sent the request
        # is the mentor (since there is only one by definition, we don't need
        # an id for the mentor)
        pairing = Pairing.objects.filter(terminated=False).filter(
            in_proposal=False).get(mentee=request.user)
        if request.method == 'GET':
            # Serialize then return the mentor
            serializer = UserSerializer(pairing.mentor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            # Update the pairing to be terminated through its serializer
            serializer = PairingSerializer(
                pairing, data={"terminated": True}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Pairing.DoesNotExist:
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
    # Get the pairings with the request user as the mentee, which are still
    # in the proposal phase
    pairings = Pairing.objects.filter(mentee=request.user).filter(
        terminated=False).filter(in_proposal=True)
    if request.method == 'GET':
        # Get a list of ids for these pairings
        mentor_ids = pairings.values_list('mentor', flat=True)
        # Get the mentor objects mapped to by the ids, and serialize and return
        # them
        mentors = User.objects.filter(id__in=mentor_ids)
        serializer = UserSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif 'mentor' in request.data:
        try:
            # Get the user object for the specified mentor
            mentor = User.objects.get(
                username__exact=request.data.get('mentor'))
            # Get the pairing with the specificed mentor
            pairing = pairings.get(mentor=mentor)
            if request.method == 'POST':
                # Update the pairing to be accepted through its serializer
                serializer = PairingSerializer(
                    pairing, data={"in_proposal": False}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                # Make feedback for the new mentor
                serializer = GeneralFeedbackSerializer(data={
                    "rating": 3,
                    "positives": "",
                    "negatives": ""
                }, context={'request': request, 'mentor': mentor})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                # Update the pairing to be terminated through its serializer
                serializer = PairingSerializer(
                    data={"terminated": True}, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, Pairing.DoesNotExist):
            return Response("Mentee or pairing does not exist", status=status.HTTP_404_NOT_FOUND)


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
        # .filter(mentee=False) # filter not self etc
        possible_mentees = User.objects.order_by('-first_name')
        serializer = UserSerializer(possible_mentees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




    elif request.method == 'POST':
        if 'mentee' in request.data:
            try:
                # Get the object for the specified mentee
                mentee = User.objects.get(
                    username__exact=request.data.get('mentee'))
                # Create the object through the serializer
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

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def feedback_mentor(request):
    """
    get:
        Get the contents of the mentor feedback.
    patch:
        Modify the mentor feedback from a user.
    """
    if request.method == 'GET':
        # Get the general feedback
        feedback = GeneralFeedback.objects.all()
        serializer = GeneralFeedbackSerializer(feedback, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH' and 'feedback_id' in request.data:
        # Get a notification by its id, then update it with the request data
        # if it is valid
        try:
            notification = GeneralFeedback.objects.get(
                id=request.data.get('feedback_id'))
            serializer = GeneralFeedbackSerializer(
                notification, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except GeneralFeedback.DoesNotExist:
            return Response("Cannot update non-existent feedback", status=status.HTTP_400_BAD_REQUEST)

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
#                 serializer = MeetingFeedbackSerializer(meeting)
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
#                     partial=True
#                 )
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             elif request.method == 'DELETE':
#                 serializer = MeetingFeedbackSerializer(
#                     data=request.data,
#                     context={'request': request, 'meeting': meeting}
#                 )
#         except Meeting.DoesNotExist:
#             return Response("Meeting does not exist", status=status.HTTP_404_NOT_FOUND)
#     return Response("No meeting provided", status=status.HTTP_400_BAD_REQUEST)


##############
### Topics ###
##############

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated]) # This could be an admin field
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
        # Get, serialize, and return all the topics
        strength_weaknesses = StrengthWeakness.objects.all()
        serializer = StrengthWeaknessSerializer(strength_weaknesses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Add a new topic through the serializer
        serializer = StrengthWeaknessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'sw_type' in request.data:
        # Get the topic by its name if it exists, and delete it
        try:
            topic = StrengthWeakness.objects.get(
                sw_type__exact=request.data.get('sw_type'))
            serializer = StrengthWeaknessSerializer(topic)
            topic.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except StrengthWeakness.DoesNotExist:
            return Response("Cannot delete non-existent topic", status=status.HTTP_400_BAD_REQUEST)

#####################
### Notifications ###
#####################


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def notifications_list(request):
    """
    get:
        Return the list of all the user's notifications.
    patch:
        Set a specific notification to be read.
    """
    if request.method == 'GET':
        # Get the list of all notifications for a user
        notifications = Notification.objects.filter(user__exact=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Create a new notification with the request data
        serializer = NotificationSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH' and 'notification' in request.data:
        # Get a notification by its id, then update it with the request data
        # if it is valid
        try:
            notification = Notification.objects.get(
                id=request.data.get('notification'))
            serializer = NotificationSerializer(
                notification, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Notification.DoesNotExist:
            return Response("Cannot update non-existent notification", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'notification' in request.data:
        # Get a notification by its id, then delete it if it is valid
        try:
            notification = Notification.objects.get(
                id=request.data.get('notification'))
            serializer = NotificationSerializer(notification)
            notification.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Notification.DoesNotExist:
            return Response("Cannot delete non-existent notification", status=status.HTTP_400_BAD_REQUEST)


################
### Meetings ###
################


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def meetings_list(request):
    """
    get:
        Get the list of all the user's scheduled meetings
    patch:
        Modify a meeting
    """
    # Get all the meetings relating to the user
    meetings = Meeting.objects.filter(Q(instructor__exact=request.user) | Q(
        mentee__exact=request.user)).order_by('-start_datetime')
    # Serialize and return all the user objects
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def meetings_request(request):
    """
    get:
        Get the list of meetings requests from a specific user
    post:
        Add a new meeting request from a specific user
    delete:
        Cancel a user's meeting request
    """
    if request.method == 'GET':
        # Serialize and return the meeting requests from the authenticated user
        meeting_requests = MeetingRequest.objects.filter(
            mentee__exact=request.user)
        serializer = MeetingRequestSerializer(meeting_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Add a new meeting request
        serializer = MeetingRequestSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'mentor' in request.data:
        try:
            # Get the appropriate meeting, and delete it
            meeting = MeetingRequest.objects.filter(mentee__exact=request.user).get(
                mentor__exact=request.data.get('mentor'))
            serializer = MeetingRequestSerializer(meeting)
            meeting.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except MeetingRequest.DoesNotExist:
            return Response("Cannot delete non-existent meeting request", status=status.HTTP_400_BAD_REQUEST)
    return Response("API not yet implemented", status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def meetings_propose(request):
    """
    get:
        Get the list of meeting requests from all the users mentees
    post:
        Add a new set of proposed times for a meeting request (delete not
        implemented due to rules of mentoring)
    """
    if request.method == 'GET':
        meeting_requests = MeetingRequest.objects.filter(
            mentor__exact=request.user).filter(is_proposed=False)
        # Serialize and return the meeting requests from the authenticated user
        serializer = MeetingRequestSerializer(meeting_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST' and 'meeting_request_id' in request.data:
        # Mark the meeting request as proposed
        try:
            meeting_request = MeetingRequest.objects.get(id=request.data.get('meeting_request_id'))
            serializer = MeetingRequestSerializer(
                meeting_request, data={"is_proposed":True}, partial=True)
            if serializer.is_valid():
                serializer.save()
            # Add a new meeting proposal
            # TODO: THIS IS NOT TOTALLY SECURE AS USER CAN CHANGE MEETING DATA
            serializer = MeetingProposalSerializer(data=request.data, context={'request': request, 'meeting_request': meeting_request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MeetingRequest.DoesNotExist:
            return Response("Cannot propose times for non-existent meeting request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def meetings_accept(request):
    """
    get:
        Get the list of meetings with proposed times for the user
    post:
        Accept one of the proposed times, and schedule the meeting
    delete:
        Indicate none of the times work, and throw the proposal back to the
        mentor to find more times
    """
    if request.method == 'GET':
        # Serialize and return the meeting proposals from the authenticated user
        meeting_requests = MeetingProposal.objects.filter(
            mentee__exact=request.user).filter(is_accepted=False).filter(is_rejected=False)
        serializer = MeetingProposalSerializer(meeting_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST' and 'meeting_proposal_id':
        # Create a new meeting at the specfifed time
        try:
            meeting_proposal = MeetingProposal.objects.get(id=request.data.get('meeting_proposal_id'))
            proposal_serializer = MeetingProposalSerializer(
                meeting_proposal, data={"is_accepted":True}, partial=True)
            if proposal_serializer.is_valid():
                proposal_serializer.save()
                return Response(proposal_serializer.data, status=status.HTTP_202_ACCEPTED)
            # Add a new meeting proposal
            # TODO: THIS IS NOT TOTALLY SECURE AS USER CAN CHANGE MEETING DATA
            meeting_serializer = MeetingSerializer(data=request.data, context={'request': request})
            if meeting_serializer.is_valid():
                meeting_serializer.save()
                return Response(meeting_serializer.data, status=status.HTTP_201_CREATED)
            return Response(meeting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MeetingProposal.DoesNotExist:
            return Response("Cannot accept non-existent meeting proposal", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'meeting_proposal_id' in request.data:
        try:
            # Mark the proposal as rejected
            meeting_proposal = MeetingProposal.objects.get(id=request.data.get('meeting_proposal_id'))
            serializer_proposal = MeetingProposalSerializer(
                meeting_proposal, data={"is_rejected":True}, partial=True)
            if serializer_proposal.is_valid():
                serializer_proposal.save()
            # Re-open the meeting request
            meeting_request = meeting_proposal.request
            serializer_request = MeetingRequestSerializer(
                meeting_request, data={"is_proposed":False}, partial=True)
            if serializer_request.is_valid():
                serializer_request.save()
                return Response(serializer_proposal.data, status=status.HTTP_201_CREATED)
        except MeetingProposal.DoesNotExist:
            return Response("Cannot accept non-existent meeting proposal", status=status.HTTP_400_BAD_REQUEST)
    return Response("API not yet implemented", status=status.HTTP_200_OK)
    # return Response("Required data values not received", status=status.HTTP_400_BAD_REQUEST)



####################
### Group events ###
####################

#######################
### Plans of action ###
#######################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def plan_of_action_list(request):
    """
    get:
        Get the contents of the user's plan of action; a list of all their
        milestones.
    """
    # Get all the user's milestone objects ordered by creation date
    milestones = Milestone.objects.filter(
        user=request.user).order_by('-creation_datetime')
    # Serialize and return all the user milestones
    serializer = MilestoneSerializer(milestones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def plan_of_action_milestone(request):
    """
    get:
        Get the contents of the milestone.
    post:
        Add a milestone to the user's plan of action.
    patch:
        Modify a user's milestone, including marking it as complete.
    delete:
        Delete a user's milestone.
    """
    if request.method == 'GET' and 'milestone' in request.data:
        try:
            # Serialize then return the milestone with the specified id
            milestone = Milestone.objects.get(id=request.data.get('milestone'))
            serializer = MilestoneSerializer(milestone)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Milestone.DoesNotExist:
            return Response("Milestone does not exist", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        # Create a new milestone with the request data
        serializer = MilestoneSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH' and 'milestone' in request.data:
        # Get a milestone by its id, then update it with the request data
        # if it is valid
        try:
            notification = Milestone.objects.get(
                id=request.data.get('milestone'))
            serializer = MilestoneSerializer(
                notification, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Milestone.DoesNotExist:
            return Response("Cannot update non-existent milestone", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' and 'milestone' in request.data:
        # Get a notification by its id, then delete it if it is valid
        try:
            milestone = Milestone.objects.get(id=request.data.get('milestone'))
            serializer = MilestoneSerializer(milestone)
            milestone.delete()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Milestone.DoesNotExist:
            return Response("Cannot delete non-existent milestone", status=status.HTTP_400_BAD_REQUEST)
