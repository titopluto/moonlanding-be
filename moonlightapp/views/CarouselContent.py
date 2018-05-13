from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from moonlightapp.models.CarouselContent import CarouselContent as CarouselContentModel
from moonlightapp.serializers.CarouselContent import CarouselContentList as CarouselContentListSerializer

class CarouselContentList(APIView):
    """
    List all Carousel Content.
    """
    def get(self, request, format=None):
        content = CarouselContentModel.objects.filter(active=True)
        serializer = CarouselContentListSerializer(content, many=True)

        return Response(serializer.data)