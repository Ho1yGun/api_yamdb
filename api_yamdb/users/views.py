from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import UserSerializer, SignUpSerializer
from .models import User, SignUp, generate_confirmation_code

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username')


class RegisterView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid() and serializer.validated_data['username'] != 'me':
            serializer.save()
            confirmation_code = generate_confirmation_code()
            send_mail(
                'код',
                f'Введите этот код для завершения регистрации: {confirmation_code}',
                'noreply@gmail.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token(user, reqister):
    serializer = UserSerializer
    User.objects.create(username = serializer.validated_data['username'],
    password = serializer.validated_data['password'],
    first_name = serializer.validated_data['first_name'],
    last_name = serializer.validated_data['last_name'],
    bio = serializer.validated_data['bio'],
    code = serializer.validated_data['code'],
    role = serializer.validated_data['role'],
    email = serializer.validated_data['email'])
    if serializer.code == RegisterView.code:
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
        }
