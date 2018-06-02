from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from moonlightapp.models.Pod import Pod as PodModel
from moonlightapp.models.Device import Device as DeviceModel
from moonlightapp.models.PodDevice import PodDevice as PodDeviceModel
from moonlightapp.serializers.Pod import PodList as PodListSerializer
from moonlightapp.serializers.Pod import PodDetail as PodDetailSerializer

class PodList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all Pods.
    """
    def get(self, request, format=None):
        pods = PodModel.objects.all()
        serializer = PodListSerializer(pods, many=True)

        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = PodSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #


class PodDetail(APIView):
    permission_classes = (IsAuthenticated,)
    """
       Retrieve Pod instance.
    """

    def get_object(self, pk):
        try:
            return PodModel.objects.get(pk=pk)
        except PodModel.DoesNotExist:
            raise Http404

    def get_device(self, pk):
        try:
            return DeviceModel.objects.get(pk=pk)
        except DeviceModel.DoesNotExist:
            raise Http404

    def get_pod_device(self, pk):
        # try:
            return PodDeviceModel.objects.filter(pod=pk)
        # except PodDeviceModel.DoesNotExist:
        #     raise Http404

    def get(self, request, pk=None, format=None):
        print(pk)
        pod = self.get_object(pk)
        serializer = PodDetailSerializer(pod)
        return Response(serializer.data)

    # def post(self, request, pk=None, format=None):
    #     pod = self.get_object(pk)
    #     print(request.data)
    #     for i in self.get_pod_device(pod):
    #         i.delete()
    #     for dev in request.data["devices"]:
    #         print(type(dev["device"]["id"]))
    #         devv = self.get_device(dev["device"]["id"])
    #         PodDeviceModel(device = devv, pod = pod, dev_url = dev["dev_url"]).save()
    # 
    #     return self.get(request, pk)