from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import *

# https://www.geeksforgeeks.org/function-based-views-django-rest-framework/ (primary - 2nd half)
# https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/ (unread another)
# https://www.bezkoder.com/django-rest-api/ (less useful)

# https://www.django-rest-framework.org/topics/documenting-your-api/ (for future)


#####################
### USER ACCOUNTS ###
#####################
# register - done
# login
# resetPassword
# getProfile - done
# (updateProfile) - done
#####################

@api_view(['GET'])
def user_profile_list(request):
    """
    User profile list api endpoint
        - GET:  Return the list of all user profiles
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register(request):
    """
    User registration api endpoint
        - POST: Register a new user account
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # When we do authentication, this should also return an auth token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_profile(request, email):
    """
    User single profile api endpoint
        - GET:  Return the user profile for a specific email
        - POST: Update the user profile data for a specific email
                TODO: Could be a PATCH type, need old email selector if email is what is being updated!
    """
    try:
        user = User.objects.get(email__exact=email) # TODO: This should probably be done over post? and needs auth token permissions
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
# (getStrengthsWeaknesses) - done
# (updateStrengthsWeaknesses) - done
############################

@api_view(['GET', 'POST'])
def strength_weaknesses(request):
    """
    Strength/weakness topics api endpoint
        - GET:  Return all the strength/weakness topics
        - POST: Add a new strength/weakness topic
                TODO: Could be a CREATE type
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

#######################
###    MENTORING    ###
#######################
# mentor -> (selectMentor, getMentor, terminateRelationship)
# mentee -> (getMentees, acceptMentee, terminateRelationship)
# proposed_mentees -> (getRequestedMentees, accept_mentee (, withdrawRequest))
# potential_mentors
#######################

@api_view(['GET', 'POST', 'DELETE'])
def mentor(request):
    """
    Mentor api endpoint
        - GET:  Return the mentor of a specific user
        - POST: Accept the offer of mentoring from a mentor for a specific user
                TODO: Could be a CREATE type
        - DELETE: Terminate the relationship with a mentor of a specific user
    """
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def mentees(request):
    """
    Mentee api endpoint
        - GET:  Return the mentees of a specific user
        - POST: Offer mentoring to a specific user from a specific user
                TODO: Could be a CREATE type
        - DELETE: Terminate the relationship with a specific mentee of a specific user
    """
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    return Response("API not yet implemented", status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def proposed_mentees(request):
    """
    Proposed mentees api endpoint
        - GET:  Return the mentees requesting mentorship from a specific user
        - POST: Accept the request to mentor a specific user of a specific user
                TODO: Could be a CREATE type
        - DELETE: Withdraw the request of a specific user to be mentored by a specific user
    """
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    return Response("API not yet implemented", status=status.HTTP_200_OK)

@api_view(['GET'])
def potential_mentees(request):
    """
    Potential mentees list api endpoint
        - GET:  Return the ordered list of possible mentees for a specific user.
                This forms the crux of the matching system
            # TODO: Offer pagination for number of possible mentees?
    """
    if request.method == 'GET':
        return Response("API not yet implemented", status=status.HTTP_200_OK)






################################################################################
################################################################################
################################################################################





# register
# login
# resetPassword
# resetPassword
# getProfile
# getPotentialMentors
# selectMentor
# getRequestedMentees
# acceptMentee
# getMentor
# getMentees
# terminateRelationship
# proposeMeeting
# proposeMeetingTimes
# acceptMeeting
# reproposeMeeting
# cancelMeeting
# getMeetings
# giveMeetingFeedback
# getPlanOfAction
# addMilestone
# setMilestone
# completeMilestone
# getMilestone
# setMentorFeedback
# createGroupEvent
# specified
# getGroupEvent
# joinGroupEvent
# getNotifications
# submitSiteFeedback

#####################
### USER ACCOUNTS ###
#####################
# register - done
# login
# resetPassword
# getProfile - done
# (updateProfile) - done
#####################

############################
### STRENGTHS WEAKNESSES ###
############################
# (getStrengthsWeaknesses) - done
# (updateStrengthsWeaknesses) - done
############################

#######################
###    MENTORING    ###
#######################
# getPotentialMentors
# selectMentor
# getRequestedMentees
# acceptMentee
# getMentor
# getMentees
# terminateRelationship
#######################

########################
###     MEETINGS     ###
########################
# proposeMeeting
# proposeMeetingTimes
# acceptMeeting
# reproposeMeeting
# cancelMeeting
# getMeetings
########################

#######################
### PLANS OF ACTION ###
#######################
# getPlanOfAction
# addMilestone
# setMilestone
# completeMilestone
# getMilestone
#######################

#######################
### PLANS OF ACTION ###
#######################
# giveMeetingFeedback
# setMentorFeedback
# submitSiteFeedback
#####################

####################
### GROUP EVENTS ###
####################
# createGroupEvent
# getGroupEvent
# joinGroupEvent
####################

#####################
### NOTIFICATIONS ###
#####################
# getNotifications
####################
