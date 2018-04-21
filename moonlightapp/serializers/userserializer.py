from rest_framework import serializers
from moonlightapp.models.usermodel import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("name",)