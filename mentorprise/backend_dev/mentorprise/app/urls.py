from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from app import views

urlpatterns = [
    ############
    ### User ###
    ############
    path('users/profiles/', views.user_profile_list),
    path('users/register/', views.user_register),
    path('users/login/', obtain_auth_token),
    path('users/logout/', views.user_logout),
    path('users/profile/', views.user_profile),
    path('users/account/', views.user_account),
    path('users/password/', views.user_password),
    path('users/delete/', views.user_delete),

    #################
    ### Mentoring ###
    #################
    path('mentoring/mentees/', views.mentoring_mentees_list),
    path('mentoring/mentee/', views.mentoring_mentee),
    path('mentoring/mentor/', views.mentoring_mentor),
    path('mentoring/proposed_mentors/', views.mentoring_proposed_mentors),
    path('mentoring/potential_mentees/', views.mentoring_potential_mentees_list),

    ################
    ### Feedback ###
    ################
    path('feedback/system/', views.feedback_system),
    # path('feedback/meetings/', views.feedback_meeting),
    # path('feedback/group_events/', views.feedback_group_event),
    # path('feedback/mentor/', views.feedback_mentor),

    ################
    ### Meetings ###
    ################
    # path('meetings/', views.meetings_list),
    # path('meetings/request/', views.meetings_request),
    # path('meetings/propose/', views.meetings_propose),
    # path('meetings/accept/', views.meetings_accept),

    ####################
    ### Group events ###
    ####################
    # path('group_events/', views.group_events_list),
    # path('group_events/make/', views.group_events_make),
    # path('group_events/join/', views.group_events_join),

    #######################
    ### Plans of action ###
    #######################
    path('plans_of_action/', views.plan_of_action_list),
    path('plans_of_action/milestones/', views.plan_of_action_milestone),

    ##############
    ### Topics ###
    ##############
    path('topics/', views.topics),

    #####################
    ### Notifications ###
    #####################
    path('notifications/', views.notifications_list),
]
