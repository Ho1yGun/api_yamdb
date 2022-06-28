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
from .models import User, ConfirmationCode, generate_confirmation_code

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username')


class RegisterView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            User.objects.create_user(username=serializer.validated_data['username'],
            email=serializer.validated_data['email'])
            confirmation_code = generate_confirmation_code()
            ConfirmationCode.objects.create(code=confirmation_code, username = serializer.validated_data['username'])
            send_mail(
                'код',
                f'Введите этот код для завершения регистрации: {confirmation_code}',
                'noreply@gmail.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token(user):
    serializer = UserSerializer
    confirmation_code = ConfirmationCode.objects.filter(username=user)
    code = confirmation_code.code
    if serializer.validated_data['code'] == code:
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
        }
