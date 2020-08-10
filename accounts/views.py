from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import generics

from accounts.models import User
from accounts.serializers import UserSerializer
# Also add these imports
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        user = self.request.user
        print(user)
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# class Vendorlisting(generics.ListAPIView):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get_vendor(self):

#         u = User.objects.filter(is_seller=True)
#         data = UserSerializer(data=u).data

#         return data

# class VendorList(generics.ListAPIView):

#     serializer_class = UserSerializer

#     def get_queryset(self):

#         user = self.request.user
#         return User.objects.filter(is_seller=True)


class VendorList(generics.ListAPIView):

    serializer_class = UserSerializer
    model = User

    @classmethod
    def get_extra_actions(cls):

        return []

    def get_queryset(self):

        queryset = User.objects.filter(is_seller=True)

        return queryset
