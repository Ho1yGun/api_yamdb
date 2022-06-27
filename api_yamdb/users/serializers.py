from rest_framework import serializers
from .models import User, SignUp


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ("username", "email")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name", "bio", "role", "code")
