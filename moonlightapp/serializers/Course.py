from rest_framework import serializers

from moonlightapp.models.Course import Course as CourseModel
from moonlightapp.models.Lab import Lab as LabModel

class Lab(serializers.ModelSerializer):

    class Meta:
        model = LabModel
        fields = ('id', 'name', 'description', 'manual_file')


class CourseLabList(serializers.ModelSerializer):
    lab = Lab(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'lab')


class CourseList(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        fields = ('id', 'name')