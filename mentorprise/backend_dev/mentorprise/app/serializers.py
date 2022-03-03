from dataclasses import field
from rest_framework import serializers
from app.models import *

class StrengthWeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthWeakness
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    expert_at = StrengthWeaknessSerializer()
    class Meta:
        model = Profile
        fields = ['biography', 'business_area', 'job_title', 'expert_at', 'mentor']

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
