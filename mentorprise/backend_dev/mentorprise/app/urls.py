from django.urls import path
from app import views

urlpatterns = [
    path('profiles/',
         views.user_profile_list,
         name = 'user-list'),
    path('register/',
         views.register,
         name = 'user-register'),
    path('profiles/<str:email>/',
         views.user_profile,
         name = 'user-detail'),

    path('strengths_weaknesses/',
         views.strength_weaknesses,
         name = 'strength-weaknesses-list'),

    path('mentor/',
         views.mentor,
         name = 'mentor-detail'),
    path('mentees/',
         views.mentees,
         name = 'mentees-list'),
    path('proposed_mentees/',
         views.proposed_mentees,
         name = 'proposed-mentees-list'),
    path('potential_mentees/',
         views.potential_mentees,
         name = 'potential-mentees-list'),
]
