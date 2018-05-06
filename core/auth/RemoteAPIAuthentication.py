import requests
import json
import django.contrib.auth as auth
import django.contrib.auth.signals as signals
from django.contrib.auth.models import User

headers = {'content-type': 'application/json'}

AUTH_API = "http://access.inwk.dal.ca/api/api-token-auth/"
TOKEN_VERIFY = "http://access.inwk.dal.ca/api/api-token-verify/"

def token_decode(token):
    user = User(id = 13, username = "username", email = "email")
    return user

def authenticate(request=None, **credentials):
    print(credentials)
    data = {}
    data["username"] = credentials["username"]
    data["password"] = credentials["password"]
    res = requests.post(AUTH_API, data=json.dumps(data), headers=headers)

    statusCode = res.status_code

    if statusCode == 200:
        res_obj = res.json()
        return token_decode(res_obj)
    elif statusCode == 401:
        # The credentials supplied are invalid to all backends, fire signal
        signals.user_login_failed.send(sender=__name__, credentials=auth._clean_credentials(credentials), request=request)