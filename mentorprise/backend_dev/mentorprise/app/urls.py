from django.urls import path
from app import views

urlpatterns = [
    path('users/',
         views.user_list,
         name = 'user-list'),
    path('users/<int:pk>/',
         views.user_detail,
         name = 'user-detail'),
]
