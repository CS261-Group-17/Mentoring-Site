from django.urls import path
from app import views

urlpatterns = [
    ############
    ### User ###
    ############
    path('users/profiles/', views.user_profile_list, name='user-profiles-list'),
    path('users/profile/<str:user_id>/', views.user_profile, name='user-profile'),
    path('users/register/', views.user_register, name='user-register'),
    path('users/login/', views.user_login, name='user-login'),
    path('users/delete/<str:user_id>/', views.user_delete, name='user-delete'),
    path('users/email/<str:user_id>/', views.user_email, name='user-email'),
    path('users/password/<str:user_id>/', views.user_password, name='user-password'),

    ##############
    ### Topics ###
    ##############

    #####################
    ### Notifications ###
    #####################

    ################
    ### Feedback ###
    ################

    ####################
    ### Group events ###
    ####################

    #######################
    ### Plans of action ###
    #######################

    ################
    ### Meetings ###
    ################

    #################
    ### Mentoring ###
    #################

]



    # path('register/',
    #      views.register,
    #      name = 'user-register'),
    # path('profiles/<str:email>/',
    #      views.user_profile,
    #      name = 'user-detail'),

    # path('strengths_weaknesses/',
    #      views.strength_weaknesses,
    #      name = 'strength-weaknesses-list'),

    # path('mentor/',
    #      views.mentor,
    #      name = 'mentor-detail'),
    # path('mentees/',
    #      views.mentees,
    #      name = 'mentees-list'),
    # path('proposed_mentees/',
    #      views.proposed_mentees,
    #      name = 'proposed-mentees-list'),
    # path('potential_mentees/',
    #      views.potential_mentees,
    #      name = 'potential-mentees-list'),
