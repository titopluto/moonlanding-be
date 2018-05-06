from django.contrib.auth.models import User, AnonymousUser
from rest_framework import authentication
from rest_framework import exceptions

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        request
        print("asdfadfsafsafsd")
        if not username:
            return None
        username = "kulwant"
        email = "kulwant@dal.ca"
        first_name = "kulwant"
        last_name = "singh"
        try:
            user = User(username=username, email = email, first_name = first_name, last_name = last_name)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)