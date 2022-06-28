from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.views import APIView

from .serializers import UserSerializer, SignUpSerializer
from .models import User, SignUp, generate_confirmation_code

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            confirmation_code = generate_confirmation_code()
            send_mail(
                'код',
                f'Введите этот код для завершения регистрации: {confirmation_code}',
                'noreply@gmail.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token(user, reqister):
    serializer = UserSerializer
    User.objects.create(username = serializer.validated_data['email'],
    password = serializer.validated_data['password'],
    first_name = serializer.validated_data['first_name'],
    last_name = serializer.validated_data['last_name'],
    bio = serializer.validated_data['bio'],
    code = serializer.validated_data['code'],
    email = serializer.validated_data['email'])
    if serializer.code == RegisterView.code:
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
        }
