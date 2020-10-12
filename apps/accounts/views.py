from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import generics

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer, VendorListingSeializer
from apps.accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        user = self.request.user
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class VendorList(generics.ListAPIView):

    serializer_class = VendorListingSeializer
    model = User

    # @classmethod
    # def get_extra_actions(cls):

    #     return []

    def get_queryset(self):

        queryset = User.objects.filter(is_seller=True)

        return queryset
