from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Confirm


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "bio", "role")


class ConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirm
        fields = ("user", "confirmation_code")


# class UserEditSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ("username", "email", "first_name",
#                   "last_name", "bio", "role")
#         model = User
#         read_only_fields = ('role',)
#
#
# class RegisterDataSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#         validators=[
#             UniqueValidator(queryset=User.objects.all())
#         ]
#     )
#     email = serializers.EmailField(
#         validators=[
#             UniqueValidator(queryset=User.objects.all())
#         ]
#     )
#
#     def validate_username(self, value):
#         if value.lower() == "me":
#             raise serializers.ValidationError("Username 'me' is not valid")
#         return value
#
#     class Meta:
#         fields = ("username", "email")
#         model = User
#
#
# class TokenSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     confirmation_code = serializers.CharField()
