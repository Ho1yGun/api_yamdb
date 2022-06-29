from django.urls import include, path
from rest_framework import routers
from .views import RegisterView, UserViewSet

app_name = 'users'


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
]
