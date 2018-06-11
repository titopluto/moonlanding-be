from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from random import randint

from .PasswordSerializer import PasswordSerializer
from .LDAP import changePassword, reset_password
from .auth.tokens import RefreshToken, PasswordResetToken, Token
from .auth.utils import create_user_obj
from .ResponseStatus import ResponseStatus
from .auth.settings import api_settings
from .EmailService import send_email

class Password(APIView):
    permission_classes = (IsAuthenticated,)
    """
    put:
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


class PasswordResetEmail(APIView):

    def post(self, request):
        email = request.data["email"]
        id = randint(1, 100)
        user = create_user_obj(id, email)
        token = str(PasswordResetToken.for_user(user))
        try:
            send_email(to=email, content=token)
            res_status = ResponseStatus(200, "SUCCESS", "Password Reset email has been sent")
            return Response(res_status.__dict__, status=res_status.status_code)
        except Exception as e:
            res_status = ResponseStatus(500, "FAILURE", e.args[0])
            return Response(res_status.__dict__, status=res_status.status_code)

class PasswordReset(APIView):

    def post(self, request):
        data = request.data
        raw_token = data["token"]
        password = data["password"]

        try:
            token = PasswordResetToken(raw_token)
            email = token[api_settings.USER_USERNAME_CLAIM]
            res_status = reset_password(email, password)
            return Response(res_status.__dict__, status=res_status.status_code)
        except Exception as e:
            res_status = ResponseStatus(500, "FAILURE", e.args[0])

        return Response(res_status.__dict__, status=res_status.status_code)


