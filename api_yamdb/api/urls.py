from django.urls import include, path
from rest_framework import routers
from users.views import GetTokenView, RegisterView, UserViewSet

from .views import (CategoryViwSet, CommentsViewSet, GenreViewSet,
                    ReviewsViewSet, TitleViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register(
    'categories',
    CategoryViwSet,
    basename='categories'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)

router_v1.register(
    'users',
    UserViewSet,
    basename='users'
)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', RegisterView.as_view(), name='signup'),
    path('v1/auth/token/', GetTokenView.as_view(), name='token'),
    path('v1/auth/', include('users.urls', namespace='users')),
    path('v1/auth/', include('django.contrib.auth.urls')),
]
