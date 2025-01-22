from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a snippet to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, or OPTIONS requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions only to the owner of the snippet
        return obj.owner == request.user
