from rest_framework import permissions


class IsDealerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow dealers of an object to edit it.
    Assumes the model instance has an `dealer` attribute.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return (obj.dealer == request.user) or request.user.is_superuser
        # return obj.dealer == request.user
