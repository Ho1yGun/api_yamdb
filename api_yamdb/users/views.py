from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.views import APIView

from .serializers import UserSerializer, ConfirmSerializer
from .models import User, Confirm

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if request.user.is_authenticated == False & serializer.is_valid():
            serializer.save()
            confirmation_code = Confirm.objects.create(user=request.user)
            send_mail(
                'Введите этот код для завершения регистрации:',
                f'{confirmation_code}',
                [request.user.email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_token(user, reqister):
    serializer = ConfirmSerializer
    if serializer.code == RegisterView.code:
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
        }
