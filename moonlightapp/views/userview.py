from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from moonlightapp.models.usermodel import User
from moonlightapp.serializers.userserializer import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()