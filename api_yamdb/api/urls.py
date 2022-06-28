from django.urls import include, path
from rest_framework import routers


from .views import ReviewsViewSet, CategoriesViwSet, GenresViewSet, TitlesViewSet, CommentsViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    'categories',
    CategoriesViwSet,
    basename='categories'
)
router_v1.register(
    'genres',
    GenresViewSet,
    basename='genres'
)
router_v1.register(
    'titles',
    TitlesViewSet,
    basename='titles'
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
    path('v1/', include('djoser.urls.jwt')),
    path('v1/auth/', include('users.urls', namespace='users')),
    path('v1/auth/', include('django.contrib.auth.urls')),
    path('v1/', include(router_v1.urls)),
]
