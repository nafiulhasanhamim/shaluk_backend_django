from rest_framework import views, response, exceptions, permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers as user_serializer
from . import services, authentication
# from . import services

class RegisterApi(views.APIView):
    def post(self, request):
        email = request.data.get('email')

        # Check if a user with the given email already exists
        existing_user = services.user_email_selector(email)
        if existing_user:
            return response.Response(data={"message": "User with this email already exists"})

        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)
        # print(data)
        # return response.Response(data=serializer.data)
        return response.Response(data={"message":"User created Successfully"})

class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        # print(user.is_superuser)
        token = services.create_token(user_id=user.id, is_superuser=user.is_superuser)
        resp = response.Response()

        # resp.set_cookie(key="jwt", value=token, httponly=True)
        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp
        # return Response({
        #     'token':token
        # })


class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        token = request.COOKIES.get("jwt")
        resp.delete_cookie("jwt")
        token = request.COOKIES.get("jwt")
        resp.data = {"message": "so long farewell"}

        return resp
    

from .serializers import UserSerializer
from .models import User
class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    serializer_class = UserSerializer
    queryset = User.objects.all()