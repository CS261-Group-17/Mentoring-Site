from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'biography', 'email', 'business_area', 'job_title', 'expert_at', 'mentor']
        # fields = model.__dict__["__doc__"].split("(")[1][:-1].split(", ") # Get all member variables

class StrengthWeaknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrengthWeakness
        fields = ['sw_type']
