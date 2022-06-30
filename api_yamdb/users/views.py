from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import UserSerializer, SignUpSerializer, TokenSerializer
from .models import User, generate_token

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
            user = User.objects.create_user(username=serializer.validated_data.get('username'),
            email=serializer.validated_data['email'])
            confirmation_code = generate_token.make_token(user)
            user.is_active = False
            user.save()
            send_mail(
                'код',
                f'Введите этот код для завершения регистрации: {confirmation_code}',
                'noreply@gmail.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Token_View(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = serializer.validated_data.get('confirmation_code')
            username = serializer.validated_data.get('username')
            user = get_object_or_404(User, username=username)
            if generate_token.check_token(user, confirmation_code):
                user.is_active = True
                user.save()
                token = AccessToken.for_user(user)
                return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
            return Response(
                {'confirmation_code': 'Код не действителен.'},
                status=status.HTTP_400_BAD_REQUEST
            )