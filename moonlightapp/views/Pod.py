from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from moonlightapp.models.Pod import Pod as PodModel
from moonlightapp.serializers.Pod import PodList as PodListSerializer
from moonlightapp.serializers.Pod import PodDetail as PodDetailSerializer

class PodList(APIView):
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
    """
       Retrieve Pod instance.
    """

    def get_object(self, pk):
        try:
            return PodModel.objects.get(pk=pk)
        except PodModel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        print(pk)
        pod = self.get_object(pk)
        serializer = PodDetailSerializer(pod)
        return Response(serializer.data)