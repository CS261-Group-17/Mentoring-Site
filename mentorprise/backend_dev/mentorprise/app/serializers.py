from dataclasses import field
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
        fields = ['first_name', 'last_name', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'

# class MeetingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meeting
#         fields = '__all__'

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
#         weakness_list = [GroupEventWeaknesses(weakness_type=item, event=group_event) for item in weakness_data]
#         GroupEventWeaknesses.objects.bulk_create(weakness_list)
#         return group_event
             
