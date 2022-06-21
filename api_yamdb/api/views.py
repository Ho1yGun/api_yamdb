<<<<<<< HEAD
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAuthorOrReadOnly
from api.serializers import ReviewsSerializer
from rest_framework.permissions import IsAuthenticated
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
=======
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from reviews.models import Categories, Genres, Titles
from .serializers import CategoriesSerializer, GenresSerializer, TitlesSerializer


class CategoriesViwSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer

>>>>>>> b0ed1dd (Versia_1)
