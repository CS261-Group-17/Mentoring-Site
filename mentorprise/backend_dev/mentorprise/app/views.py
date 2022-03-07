from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import *

# Django REST APIs
# https://www.geeksforgeeks.org/function-based-views-django-rest-framework/ (primary - 2nd half)
# https://www.django-rest-framework.org/topics/documenting-your-api/ (for future)

# General REST API design
# https://hub.packtpub.com/what-are-rest-verbs-and-status-codes-tutorial/
# https://www.freecodecamp.org/news/rest-api-best-practices-rest-endpoint-design-examples/


############
### User ###
############

@api_view(['GET'])
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
def user_profile(request, user_id):
    """
    An API endpoint for a specific user's profile
        - GET:      Get the contents of the user's profile
        - PATCH:    Update the contents of the user's profile
    """
    try:
        user = User.objects.get(email__exact=user_id) # TODO: Should this be done over post? and needs auth token permissions
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
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
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # When we do authentication, this should also return an auth token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    """
    An API endpoint to log in a user
        - POST:     Log in a user
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['DELETE'])
def user_delete(request, user_id):
    """
    An API endpoint to delete a specific user's account
        - DELETE:     Delete a user account
    """
    try:
        user = User.objects.get(email__exact=user_id) # TODO: Should this be done over post? and needs auth token permissions
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = UserSerializer(user)
        user.delete()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'PUT'])
def user_email(request, user_id):
    """
    An API endpoint for a specific user's email
        - GET:      Get the user's email
        - PUT:      Update the user's email
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['PUT'])
def user_password(request, user_id):
    """
    An API endpoint for a specific user's password
        - PUT:      Update the user's password
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

##############
### Topics ###
##############

@api_view(['GET', 'POST', 'DELETE'])
def topics_list(request):
    """
    An API endpoint for topics of strengths/weaknesses
        - GET:      Get the list of all topics of strengths/weaknesses
        - POST:     Add a topic of strengths/weaknesses
        - DELETE:   Delete a topic of strengths/weaknesses
    """
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

@api_view(['DELETE'])
def topic_delete(request, sw_type):
    """
    An API endpoint to delete a specific user's account
        - DELETE:     Delete a user account
    """
    try:
        user = StrengthWeakness.objects.get(sw_type__exact=sw_type) # TODO: Should this be done over post?
        # user = StrengthWeakness.objects.filter(sw_type__exact=sw_type)[0] # TODO: Should this be done over post?
    except StrengthWeakness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = StrengthWeaknessSerializer(user)
        user.delete()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#####################
### Notifications ###
#####################

@api_view(['GET'])
def notifications_list(request, user_id):
    """
    An API endpoint for a specific user's notifications
        - GET:      Get the list of all the user's notifications
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

################
### Feedback ###
################

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def feedback_meeting(request, user_id, meeting_id):
    """
    An API endpoint for a specific user's feedback on a specific meeting
        - GET:      Get the contents of the meeting feedback
        - POST:     Add a new meeting feedback from a user
        - PATCH:    Modify the meeting feedback from a user
        - DELETE:   Delete a the user's meeting feedback
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH'])
def feedback_mentor(request, user_id):
    """
    An API endpoint for a specific user's feedback on their mentor
        - GET:      Get the contents of the mentor feedback
        - PATCH:    Modify the mentor feedback from a user
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def feedback_system(request, user_id):
    """
    An API endpoint for a specific user's feedback on the system
        - GET:      Get the contents of the system feedback
        - POST:     Add a new system feedback from a user
        - DELETE:   Delete a the user's system feedback
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

####################
### Group events ###
####################

@api_view(['GET'])
def group_events_list(request, user_id):
    """
    An API endpoint for a specific user's suggestions for group events they
    could attend
        - GET:      Get the list of group events the user could attend
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def group_events_make(request, user_id):
    """
    An API endpoint for a specific user making group events
        - GET:      Get the list of group events a user is running
        - POST:     Add a new group event the user is running
        - DELETE:   Cancel a group event the user is running
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def group_events_join(request, used_id):
    """
    An API endpoint for a specific user joining group events
        - GET:      Get the list of group events a user is attending
        - POST:     Add a new group event the user is attending
        - DELETE:   Cancel a user's intention to attend a group event
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

#######################
### Plans of action ###
#######################

@api_view(['GET'])
def plan_of_action_list(request, user_id):
    """
    An API endpoint for a specific user's plan of action
        - GET:      Get the contents of the user's plan of action; a list of all
                    their milestones
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def plan_of_action_milestone(request, user_id, milestone_id):
    """
    An API endpoint for a specific user's specific milestone
        - GET:      Get the contents of the milestone
        - POST:     Add a milestone to the user's plan of action
        - PATCH:    Modify a user's milestone, including marking it as complete
        - DELETE:   Delete a user's milestone
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

################
### Meetings ###
################

@api_view(['GET'])
def meetings_list(request, user_id):
    """
    An API endpoint for a specific user's scheduled meetings
        - GET:      Get the list of all the user's scheduled meetings
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def meetings_request(request, user_id):
    """
    An API endpoint for a specific user requesting meetings with their mentor
        - GET:      Get the list of meetings requests from a specific user
        - POST:     Add a new meeting request from a specific user
        - DELETE:   Cancel a user's meeting request
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def meetings_propose(request, user_id):
    """
    An API endpoint for a specific user proposing times for meetings their
    mentee requested with them. Note no delete option to fulfill mentoring rules
        - GET:      Get the list of meeting requests from all the users mentees
        - POST:     Add a new set of proposed times for a meeting request
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def meetings_accept(request, user_id):
    """
    An API endpoint for a specific user accepting meeting times proposed for
    their requested meeting by their mentor
        - GET:      Get the list of meetings with proposed times for the user
        - POST:     Accept one of the proposed times, and schedule the meeting
        - DELETE:   Indicate none of the times work, and throw the proposal back
                    to the mentor to find more times
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

#################
### Mentoring ###
#################

@api_view(['GET'])
def mentoring_mentees_list(request, user_id):
    """
    An API endpoint for a specific user's mentees
        - GET:      Get the list of all the user's mentees
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def mentoring_mentee(request, user_id, mentee_id):
    """
    An API endpoint for a specific user's mentee
        - GET:      Get the profile of the mentee
        - DELETE:   Terminate the relationship with the mentee
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def mentoring_mentor(request, user_id):
    """
    An API endpoint for a specific user's mentor
        - GET:      Get the profile of the mentor
        - DELETE:   Terminate the relationship with the mentor
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def mentoring_proposed_mentors(request, user_id):
    """
    An API endpoint for a specific user's mentor
        - GET:      Get the list of mentors offering mentorship
        - POST:     Accept a mentor's offer of mentoring
        - DELETE:   Decline a mentor's offer of mentoring
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET'])
def mentoring_potential_mentees_list(request, user_id):
    """
    An API endpoint for an ordered list of the users a specific user might
    mentor
        - GET:      Get the ordered list of possible mentees
    """
    return Response("API not yet implemented", status=status.HTTP_200_OK)
