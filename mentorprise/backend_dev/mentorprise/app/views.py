from rest_framework import viewsets
from rest_framework import permissions

from app.serializers import *
from app.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class StrengthWeaknessViewSet(viewsets.ModelViewSet):
    queryset = StrengthWeakness.objects.all()
    serializer_class = StrengthWeaknessSerializer
    permission_classes = [permissions.IsAuthenticated]

class StrengthWeaknessListViewSet(viewsets.ModelViewSet):
    queryset = StrengthWeaknessList.objects.all()
    serializer_class = StrengthWeaknessListSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupEventViewSet(viewsets.ModelViewSet):
    queryset = GroupEvent.objects.all()
    serializer_class = GroupEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupEventWeaknessesViewSet(viewsets.ModelViewSet):
    queryset = GroupEventWeaknesses.objects.all()
    serializer_class = GroupEventWeaknessesSerializer
    permission_classes = [permissions.IsAuthenticated]

class MeetingWeaknessesViewSet(viewsets.ModelViewSet):
    queryset = MeetingWeaknesses.objects.all()
    serializer_class = MeetingWeaknessesSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class MeetingFeedbackViewSet(viewsets.ModelViewSet):
    queryset = MeetingFeedback.objects.all()
    serializer_class = MeetingFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupEventFeedbackViewSet(viewsets.ModelViewSet):
    queryset = GroupEventFeedback.objects.all()
    serializer_class = GroupEventFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class GeneralFeedbackViewSet(viewsets.ModelViewSet):
    queryset = GeneralFeedback.objects.all()
    serializer_class = GeneralFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImprovedWeaknessesViewSet(viewsets.ModelViewSet):
    queryset = ImprovedWeaknesses.objects.all()
    serializer_class = ImprovedWeaknessesSerializer
    permission_classes = [permissions.IsAuthenticated]

class SystemFeedbackViewSet(viewsets.ModelViewSet):
    queryset = SystemFeedback.objects.all()
    serializer_class = SystemFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]

class PasswordResetViewSet(viewsets.ModelViewSet):
    queryset = PasswordReset.objects.all()
    serializer_class = PasswordResetSerializer
    permission_classes = [permissions.IsAuthenticated]

class PairingViewSet(viewsets.ModelViewSet):
    queryset = Pairing.objects.all()
    serializer_class = PairingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MeetingProposalViewSet(viewsets.ModelViewSet):
    queryset = MeetingProposal.objects.all()
    serializer_class = MeetingProposalSerializer
    permission_classes = [permissions.IsAuthenticated]
