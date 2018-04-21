from rest_framework import serializers

from moonlightapp.models.Pod import Pod as PodModel

class Pod(serializers.ModelSerializer):
    class Meta:
        model = PodModel
        fields = ('id', 'name', 'devices')