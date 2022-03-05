from rest_framework import serializers
from app.models import *

class StrengthWeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthWeakness
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


# class MeetingWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingWeaknesses
#         fields = ['weakness_type']

# class MeetingSerializer(serializers.ModelSerializer):
#     weaknesses = MeetingWeaknessesSerializer(many=True)

#     class Meta:
#         model = Meeting
#         fields = ['instructor', 'title', 'description', 'start_datetime', 'duration', 'cancelled', 'mentee', 'weaknesses']

#     def create(self, validated_data):
#         weakness_data = validated_data.pop('weaknesses')
#         meeting = Meeting.objects.create(**validated_data)
#         weakness_list = [MeetingWeaknesses(weakness_type=item['weakness_type'], event=meeting) for item in weakness_data]
#         MeetingWeaknesses.objects.bulk_create(weakness_list)
#         return meeting


# class GroupEventWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupEventWeaknesses
#         fields = ['weakness_type']

# class GroupEventSerializer(serializers.ModelSerializer):
#     weaknesses = GroupEventWeaknessesSerializer(many=True)

#     class Meta:
#         model = GroupEvent
#         fields = ['instructor', 'title', 'description', 'start_datetime', 'duration', 'cancelled', 'event_type', 'capacity', 'weaknesses']

#     def create(self, validated_data):
#         weakness_data = validated_data.pop('weaknesses')
#         group_event = GroupEvent.objects.create(**validated_data)
#         weakness_list = [GroupEventWeaknesses(weakness_type=item['weakness_type'], event=group_event) for item in weakness_data]
#         GroupEventWeaknesses.objects.bulk_create(weakness_list)
#         return group_event

# class AttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendance
#         fields = '__all__'

# class MeetingFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingFeedback
#         fields = '__all__'

# class GroupEventFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupEventFeedback
#         fields = '__all__'

# class ImprovedWeaknessesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImprovedWeaknesses
#         fields = ['weakness_type']

# class GeneralFeedbackSerializer(serializers.ModelSerializer):
#     weaknesses = ImprovedWeaknessesSerializer(many=True)

#     class Meta:
#         model = GeneralFeedback
#         fields = ['rating', 'positives', 'negatives', 'giver', 'creation_datetime', 'improved_weaknesses']

#     def create(self, validated_data):
#         weakness_data = validated_data.pop('improved_weaknesses')
#         feedback = GeneralFeedback.objects.create(**validated_data)
#         weakness_list = [ImprovedWeaknesses(weakness_type=item['weakness_type'], feedback=feedback) for item in weakness_data]
#         ImprovedWeaknesses.objects.bulk_create(weakness_list)
#         return feedback

# class SystemFeedbackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SystemFeedback
#         fields = '__all__'

# class MilestoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Milestone
#         fields = '__all__'

# class PasswordResetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordRest
#         fields = '__all__'

# class PairingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pairing
#         fields = '__all__'

# class MeetingProposalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingProposal
#         fields = '__all__'

# class MeetingRequestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MeetingRequest
#         fields = '__all__'
