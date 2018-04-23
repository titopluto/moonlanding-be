from rest_framework import serializers

from moonlightapp.models.Pod import Pod as PodModel, PodDevices
from moonlightapp.models.Device import Device as DeviceModel

class Device(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ('id', 'name')

class PodDevice(serializers.ModelSerializer):
    class Meta:
        model = PodDevices
        fields = ('dev_url',)


class Pod(serializers.ModelSerializer):
    devices = Device(many=True, read_only=True)

    class Meta:
        model = PodModel
        fields = ('id', 'name', 'devices')