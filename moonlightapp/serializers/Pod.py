from rest_framework import serializers

from moonlightapp.models.Pod import Pod as PodModel
from moonlightapp.models.PodDevice import PodDevice as PodDeviceModel
from moonlightapp.models.Device import Device as DeviceModel

class Device(serializers.ModelSerializer):

    class Meta:
        model = DeviceModel
        fields = ('id', 'name')

class PodDevice(serializers.ModelSerializer):
    device = Device()

    class Meta:
        model = PodDeviceModel
        fields = ('device', 'dev_url' )


class PodDetail(serializers.ModelSerializer):
    devices = PodDevice(many=True, read_only=True)

    class Meta:
        model = PodModel
        fields = ('id', 'name', 'devices')


class PodList(serializers.ModelSerializer):

    class Meta:
        model = PodModel
        fields = ('id', 'name')