from rest_framework import serializers
from app.models import *

##############
### Topics ###
##############

class StrengthWeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthWeakness
        fields = '__all__'

############
### User ###
############

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

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class StrengthListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthList
        exclude = ['user', 'sw_type']

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["sw_type"] = self.context["sw_type"]
        return super().create(validated_data)

class WeaknessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaknessList
        exclude = ['user', 'sw_type']

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["sw_type"] = self.context["sw_type"]
        return super().create(validated_data)

# class PasswordResetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PasswordRest
#         fields = '__all__'


#################
### Mentoring ###
#################

class PairingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pairing
        fields = '__all__'


################
### Feedback ###
################

class SystemFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemFeedback
        fields = '__all__'

class MeetingFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingFeedback
        exclude = ['giver', 'meeting']

    def create(self, validated_data):
        validated_data["giver"] = self.context["request"].user
        validated_data["meeting"] = self.context["meeting"]
        return super().create(validated_data)

class GroupEventFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEventFeedback
        exclude = ['giver', 'group_event']

    def create(self, validated_data):
        validated_data["giver"] = self.context["request"].user
        validated_data["group_event"] = self.context["group_event"]
        return super().create(validated_data)

class GeneralFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralFeedback
        exclude = ['giver', 'mentor']

    def create(self, validated_data):
        validated_data["giver"] = self.context["request"].user
        validated_data["mentor"] = self.context["mentor"]
        return super().create(validated_data)


################
### Meetings ###
################

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['mentee']

    def create(self, validated_data):
        validated_data["mentee"] = self.context["request"].user
        return super().create(validated_data)

class MeetingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRequest
        exclude = ['mentee']

    def create(self, validated_data):
        validated_data["mentee"] = self.context["request"].user
        return super().create(validated_data)

class MeetingProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProposal
        exclude = ['mentor'] # TODO: does this need meeting request?

    def create(self, validated_data):
        validated_data["mentor"] = self.context["request"].user
        validated_data["request"] = self.context["meeting_request"]
        return super().create(validated_data)


####################
### Group events ###
####################

class GroupEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEvent
        exclude = ['instructor']

    def create(self, validated_data):
        validated_data["instructor"] = self.context["request"].user
        return super().create(validated_data)

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        exclude = ['attendee_id', 'group_event']

    def create(self, validated_data):
        validated_data["attendee_id"] = self.context["request"].user
        validated_data["group_event"] = self.context["event"]
        return super().create(validated_data)

class AttendanceGetterSerializer(serializers.ModelSerializer):
    group_event = GroupEventSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'

#######################
### Plans of action ###
#######################

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        exclude = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

#####################
### Notifications ###
#####################

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
