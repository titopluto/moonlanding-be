from rest_framework import serializers

class PasswordSerializer(serializers.Serializer):

    def __init__(self):
        self.fields["old_password"] = serializers.CharField(required=True)
        self.fields["new_password"] = serializers.CharField(required=True)