from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializers import ReviewsSerializer
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly

from rest_framework import viewsets

from reviews.models import Categories, Genres, Titles
from .serializers import CategoriesSerializer, GenresSerializer, TitlesSerializer


# from reviews.models import Titles


# class ReviewsViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Titles, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()


class CategoriesViwSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsAdminOrReadOnly,)
