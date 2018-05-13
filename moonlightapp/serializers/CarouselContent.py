from rest_framework import serializers

from moonlightapp.models.CarouselContent import CarouselContent as CarouselContentModel

class CarouselContentList(serializers.ModelSerializer):

    class Meta:
        model = CarouselContentModel
        fields = ('id', 'title', 'description', 'img', 'priority')