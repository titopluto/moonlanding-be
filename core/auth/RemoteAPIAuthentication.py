import requests
import json
from random import randint
import django.contrib.auth as auth
import django.contrib.auth.signals as signals
from django.conf import settings
from .utils import token_decode, create_user_obj

headers = {'content-type': 'application/json'}

AUTH_API = settings.AUTH_API

def authenticate(request=None, **credentials):

    data = {}
    data["username"] = credentials["username"]
    data["password"] = credentials["password"]
    res = requests.post(AUTH_API, data=json.dumps(data), headers=headers)

    statusCode = res.status_code

    if statusCode == 200:
        res_obj = res.json()
        id = randint(1, 100)
        return create_user_obj(id, data["username"])
    elif statusCode == 401:
        # The credentials supplied are invalid to all backends, fire signal
        signals.user_login_failed.send(sender=__name__, credentials=auth._clean_credentials(credentials), request=request)