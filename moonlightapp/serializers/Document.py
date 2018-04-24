from rest_framework import serializers

from moonlightapp.models.Document import Document as DocumentModel

class DocumentList(serializers.ModelSerializer):

    class Meta:
        model = DocumentModel
        fields = ('id', 'name', 'file')