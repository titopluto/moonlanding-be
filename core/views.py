from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .PasswordSerializer import PasswordSerializer
from .LDAP import changePassword

class Password(APIView):
    permission_classes = (IsAuthenticated,)
    """
    To update password.
    """
    serializer_class = PasswordSerializer

    def put(self, request, format=None):
        print(request.data)
        old_pass = request.data["old_password"]
        new_pass = request.data["new_password"]
        user_name = request.user.username
        res_status = changePassword(user_name, old_pass, new_pass)

        res = Response(res_status.__dict__, status=res_status.status_code)
        return res