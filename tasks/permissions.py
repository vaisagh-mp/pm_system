from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('POST', 'PUT', 'DELETE'):
            return request.user.is_authenticated and request.user.roles == 'admin'
        return request.user.is_authenticated


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('PUT',):
            return request.user.is_authenticated and request.user.roles in ('admin', 'manager')
        if request.method in ('POST', 'DELETE'):
            return request.user.is_authenticated and request.user.roles == 'admin'
        return request.user.is_authenticated
