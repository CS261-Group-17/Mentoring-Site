from django.urls import path
from app import views

urlpatterns = [
    path('profiles/',
         views.user_list,
         name = 'user-list'),
    path('register/',
         views.register,
         name = 'user-register'),
    path('profiles/<str:email>/',
         views.get_profile,
         name = 'user-detail'),
]
