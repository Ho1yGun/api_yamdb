from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import viewsets

from reviews.models import Category, Genre, Title, Reviews
from .filters import TitleFilter
from .permissions import IsAdminOrReadOnly, OnlyAdminDeleteReviewsAndComments
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          CommentsSerializer,
                          ReviewsSerializer,
                          ReadOnlyTitleSerializer)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (OnlyAdminDeleteReviewsAndComments,)

    def get_titles(self):
        return get_object_or_404(Title, id=self.kwargs.get('titles_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_titles())

    def get_queryset(self):
        return self.get_titles().comments.all()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (OnlyAdminDeleteReviewsAndComments,)

    def get_reviews(self):
        return get_object_or_404(Reviews, id=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_reviews())

    def get_queryset(self):
        return self.get_reviews().comments.all()


class CategoryViwSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter


    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return ReadOnlyTitleSerializer
        return TitleSerializer
