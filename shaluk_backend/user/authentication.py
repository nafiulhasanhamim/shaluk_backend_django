from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from . import models

from rest_framework import permissions

class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.COOKIES.get("jwt"))
        token = request.COOKIES.get("jwt")
        # print(token)
        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            # print(payload)
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()
        return (user, None)
        # return {"user":user,"is_superuser":payload["is_superuser"]}
    


class CustomUserAuthentication2(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.COOKIES.get("jwt"))
        token = request.COOKIES.get("jwt")
        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            # print(payload)
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()
        return {"user":user,"is_superuser":payload["is_superuser"]}