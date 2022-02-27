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
]
