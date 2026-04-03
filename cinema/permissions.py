from rest_framework.permissions import BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if (request.user.is_authenticated
                and request.method in ("GET", "HEAD", "OPTIONS")):
            return True
        return False
