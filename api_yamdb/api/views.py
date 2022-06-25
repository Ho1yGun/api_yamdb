from django.shortcuts import get_object_or_404
from api.permissions import OnlyAdminDeleteReviewsAndComments
from rest_framework import viewsets
from reviews.models import Categories, Genres, Titles, Reviews
from .serializers import (
    CategoriesSerializer,
    GenresSerializer,
    TitlesSerializer,
    ReviewsSerializer,
    CommentsSerializer
)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (OnlyAdminDeleteReviewsAndComments,)

    def get_titles(self):
        return get_object_or_404(Titles, id=self.kwargs.get('titles_id'))

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


class CategoriesViwSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
