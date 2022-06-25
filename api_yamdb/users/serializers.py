from rest_framework import serializers
from .models import User, Confirm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name", "bio", "role")

class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirm
        fields = ("user", "code")