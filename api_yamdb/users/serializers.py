from rest_framework import serializers
from .models import User


class SignUpSerializer(serializers.Serializer):
    user = serializers.CharField()
    email = serializers.EmailField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name", "bio", "role", "code")
