from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from moonlightapp.models.Course import Course as CourseModel
from moonlightapp.serializers.Course import CourseList as CourseListSerializer, CourseLabList as CourseLabListSerializer

class CourseList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all Courses.
    """
    def get(self, request, format=None):
        courses = CourseModel.objects.all()
        serializer = CourseListSerializer(courses, many=True)

        return Response(serializer.data)


class CouseLabList(APIView):
    permission_classes = (IsAuthenticated,)
    """
       Get Detail of Course like getting list of labs
    """

    def get_object(self, pk):
        try:
            return CourseModel.objects.get(pk=pk)
        except CourseModel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        pod = self.get_object(pk)
        serializer = CourseLabListSerializer(pod)
        return Response(serializer.data)