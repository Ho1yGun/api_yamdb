from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Проверка наличия прав администратора."""

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_admin
