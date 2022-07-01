import random
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import permissions
import random

from .permissions import IsAdmin
from .serializers import UserSerializer, SignUpSerializer, TokenSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    filter_backends = filters.SearchFilter
    search_fields = ('=username',)
    lookup_field = 'username'

    @action(
        detail=False,
        methods=('GET', 'PATCH'),
        permission_classes=(permissions.IsAuthenticated,)
    )
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role)
        return Response(serializer.data)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            confirmation_code = random.randint(1000,9999)
            user, created = User.objects.get_or_create(
                username=username,
                email=email,
        
            )
            message = f'Код подтверждения: {confirmation_code}'
            if created:
                user.save()
                send_mail(
                    subject='Код',
                    message=message,
                    from_email=None,
                    recipient_list=(email,)
                )
                context = {
                    'username': username,
                    'email': email
                }
                return Response(context, status=status.HTTP_200_OK)
            return Response({'confirmation_code': 'Код не действителен.'}, status=status.HTTP_400_BAD_REQUEST)


class GetTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            confirmation_code = serializer.validated_data.get('confirmation_code')
            username = serializer.validated_data.get('username')
            user = get_object_or_404(User, username=username)
            if confirmation_code == user.code:
                user.save()
                refresh = RefreshToken.for_user(user)
                return Response(str(refresh.access_token), status=status.HTTP_200_OK)
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )
