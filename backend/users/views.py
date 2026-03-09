from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
