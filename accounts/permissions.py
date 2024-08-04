from rest_framework import permissions
# from rest_framework.response import Response

from pprint import pprint


class UserPermission(permissions.BasePermission):
    """
    Custom permission to only allow everybody of an object to create it.
    """

    def has_permission(self, request, view):
        if request.method.lower() == 'post':
            print(view)
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
