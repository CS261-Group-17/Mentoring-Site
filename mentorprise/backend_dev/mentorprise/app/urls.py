from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from app import views

urlpatterns = [
    path('users/profiles/', views.user_profile_list),
    path('users/register/', views.user_register),
    path('users/login/', obtain_auth_token),
    path('users/logout/', views.user_logout),
    path('users/profile/', views.user_profile),
    path('users/delete/', views.user_delete),
]


# urlpatterns = [
#     ############
#     ### User ###
#     ############
#     path('users/profiles/', views.user_profile_list, name='user-profiles-list'),
#     path('users/profile/<str:user_id>/',
#          views.user_profile, name='user-profile'),
#     path('users/register/', views.user_register, name='user-register'),
#     path('users/login/', views.user_login, name='user-login'),
#     path('users/delete/<str:user_id>/', views.user_delete, name='user-delete'),
#     path('users/email/<str:user_id>/', views.user_email, name='user-email'),
#     path('users/password/<str:user_id>/',
#          views.user_password, name='user-password'),

#     ##############
#     ### Topics ###
#     ##############
#     path('topics/', views.topics_list, name='topics-list'),
#     path('topics/<str:sw_type>', views.topic_delete, name='topic-delete'),

#     #####################
#     ### Notifications ###
#     #####################
#     path('notifications/<str:user_id>/',
#          views.notifications_list, name='notifications-list'),

#     ################
#     ### Feedback ###
#     ################
#     # TODO: There might be a neater way to do this than multiple slugs
#     path('feedback/meetings/<str:user_id>/<str:meeting_id>/',
#          views.feedback_meeting, name='feedback-meeting'),
#     path('feedback/mentor/<str:user_id>/',
#          views.feedback_mentor, name='feedback-mentor'),
#     path('feedback/system/<str:user_id>/',
#          views.feedback_system, name='feedback-system'),

#     ####################
#     ### Group events ###
#     ####################
#     path('group_events/<str:user_id>/',
#          views.group_events_list, name='group-events'),
#     path('group_events/make/<str:user_id>/',
#          views.group_events_make, name='group-events-make'),
#     path('group_events/join/<str:user_id>/',
#          views.group_events_join, name='group-events-join'),

#     #######################
#     ### Plans of action ###
#     #######################
#     path('plans_of_action/<str:user_id>/',
#          views.plan_of_action_list, name='plans-of-action'),
#     path('plans_of_action/milestones/<str:user_id>/<str:milestone_id>/',
#          views.plan_of_action_milestone, name='plans-of-action-milestones'),

#     ################
#     ### Meetings ###
#     ################
#     path('meetings/<str:user_id>/', views.meetings_list, name='meetings-list'),
#     path('meetings/request/<str:user_id>/',
#          views.meetings_request, name='meetings-request'),
#     path('meetings/propose/<str:user_id>/',
#          views.meetings_propose, name='meetings-propose'),
#     path('meetings/accept/<str:user_id>/',
#          views.meetings_accept, name='meetings-accept'),


#     #################
#     ### Mentoring ###
#     #################
#     path('mentoring/mentees/<str:user_id>/',
#          views.mentoring_mentees_list, name='mentoring-mentees-list'),
#     path('mentoring/mentee/<str:user_id>/<str:mentee_id>/',
#          views.mentoring_mentee, name='mentoring-mentee'),
#     path('mentoring/mentor/<str:user_id>/',
#          views.mentoring_mentor, name='mentoring-mentor'),
#     path('mentoring/proposed_mentors/<str:user_id>/',
#          views.mentoring_proposed_mentors, name='mentoring-proposed-mentors'),
#     path('mentoring/potential_mentees/<str:user_id>/',
#          views.mentoring_potential_mentees_list, name='mentoring-potential-mentees-list'),
# ]
