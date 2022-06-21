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