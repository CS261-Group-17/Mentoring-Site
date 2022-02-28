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
    User profile list api endpoint
        - GET:  Return the list of all user profiles
    """
    if request.method == 'GET':
        user = User.objects.all().order_by('-first_name')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def user_profile(request, user_id):
    pass

@api_view(['POST'])
def user_register(request):
    pass

@api_view(['POST'])
def user_login(request):
    pass

@api_view(['GET', 'PUT'])
def user_email(request, user_id):
    pass

@api_view(['PUT'])
def user_password(request, user_id):
    pass

##############
### Topics ###
##############

@api_view(['GET', 'POST', 'DELETE'])
def topics(request):
    pass

#####################
### Notifications ###
#####################

@api_view(['GET'])
def notifications(request, user_id):
    pass

################
### Feedback ###
################

@api_view(['GET', 'POST', 'DELETE'])
def feedback_meeting(request, meeting_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def feedback_mentor(request, mentor_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def feedback_system(request):
    pass

####################
### Group events ###
####################

@api_view(['GET'])
def group_events_list(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def group_events_make(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def group_events_join(request, used_id):
    pass

#######################
### Plans of action ###
#######################

@api_view(['GET'])
def plan_of_action(request, user_id):
    pass

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def plan_of_action_milestone(request, user_id):
    pass

################
### Meetings ###
################

@api_view(['GET'])
def meetings_list(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def meetings_request(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def meetings_propose(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def meetings_accept(request, user_id):
    pass

#################
### Mentoring ###
#################

@api_view(['GET'])
def mentoring_mentees_list(request, user_id):
    pass

@api_view(['GET', 'DELETE'])
def mentoring_mentee(request, user_id, mentee_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def mentoring_mentor(request, user_id):
    pass

@api_view(['GET', 'POST', 'DELETE'])
def mentoring_proposed_mentors(request, user_id):
    pass

@api_view(['GET'])
def mentoring_potential_mentees(request, user_id):
    pass
