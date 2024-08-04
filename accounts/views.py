from django.contrib.auth import get_user_model
# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# from rest_framework.response import Response
from accounts.permissions import UserPermission

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [UserPermission,]
