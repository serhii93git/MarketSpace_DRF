from rest_framework import generics, permissions
from .models import Users
from .serializers import UserSerializer


class UserAddView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = Users.objects.all()
    serializer_class = UserSerializer
