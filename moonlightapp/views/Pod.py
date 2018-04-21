from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from moonlightapp.models.Pod import Pod as PodModel
from moonlightapp.serializers.Pod import Pod as PodSerializer

class PodList(APIView):
    """
    List all Pods, or create a new Pod.
    """
    def get(self, request, format=None):
        pods = PodModel.objects.all()
        serializer = PodSerializer(pods, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)