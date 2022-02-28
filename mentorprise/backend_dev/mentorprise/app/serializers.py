from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'biography', 'email', 'business_area', 'job_title', 'expert_at', 'mentor']

class StrengthWeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthWeakness
        fields = ['sw_type']


# class StrengthWeaknessListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StrengthWeaknessList
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# # class EventSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Event;
# #         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class MeetingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meeting
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class GroupEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupEvent
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class GroupEventWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupEventWeaknesses
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class MeetingWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingWeaknesses
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class AttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendance
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# # class FeedbackSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Feedback
# #         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class MeetingFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingFeedback
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class GroupEventFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupEventFeedback
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class GeneralFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeneralFeedback
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class ImprovedWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImprovedWeaknesses
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class SystemFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SystemFeedback
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class MilestoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Milestone
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class PasswordResetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordReset
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class PairingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pairing
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")

# class MeetingProposalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingProposal
#         fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ")
