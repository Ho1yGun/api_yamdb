from rest_framework import permissions


class OnlyAdminDeleteReviewsAndComments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return bool(request.user and request.user.is_staff)
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)
