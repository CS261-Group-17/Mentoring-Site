"""mentorprise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app import views

# Register api endpoints
router = routers.DefaultRouter()
router.register(r'users_view', views.UserViewSet)
router.register(r'strength_weaknesses_view', views.StrengthWeaknessViewSet)
router.register(r'strength_weakness_list_view', views.StrengthWeaknessListViewSet)
router.register(r'notifications_view', views.NotificationViewSet)
router.register(r'meetings_view', views.MeetingViewSet)
router.register(r'group_event_view', views.GroupEventViewSet)
router.register(r'group_event_weaknesses_view', views.GroupEventWeaknessesViewSet)
router.register(r'meeting_weaknesses_view', views.MeetingWeaknessesViewSet)
router.register(r'attendance_view', views.AttendanceViewSet)
router.register(r'meeting_feedback_view', views.MeetingFeedbackViewSet)
router.register(r'group_event_feedback_view', views.GroupEventFeedbackViewSet)
router.register(r'general_feedback_view', views.GeneralFeedbackViewSet)
router.register(r'improved_weaknesses_view', views.ImprovedWeaknessesViewSet)
router.register(r'system_feedback_view', views.SystemFeedbackViewSet)
router.register(r'milestones_view', views.MilestoneViewSet)
router.register(r'password_resets_view', views.PasswordResetViewSet)
router.register(r'pairings_view', views.PairingViewSet)
router.register(r'meeting_proposals_view', views.MeetingProposalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), # path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
