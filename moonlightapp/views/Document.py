from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from moonlightapp.models.Document import Document as DocumentModel
from moonlightapp.serializers.Document import DocumentList as DocumentListSerializer

class DocumentList(APIView):
    """
    List all Documents pods.
    """
    def get(self, request, format=None):
        documents = DocumentModel.objects.all()
        serializer = DocumentListSerializer(documents, many=True)

        return Response(serializer.data)