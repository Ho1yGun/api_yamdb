from django.urls import include, path
from rest_framework import routers

from .views import ReviewsViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews')
""" router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments') """

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
