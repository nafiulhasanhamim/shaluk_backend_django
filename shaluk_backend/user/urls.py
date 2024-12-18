from django.urls import path
from rest_framework.routers import DefaultRouter

from . import apis

urlpatterns = [
    path("register/", apis.RegisterApi.as_view(), name="register"),
    path("login/", apis.LoginApi.as_view(), name="login"),
    path("me/", apis.UserApi.as_view(), name="me"),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),
]


router = DefaultRouter()
router.register(r"users", apis.UserViewSet, basename="users")
urlpatterns += router.urls

# router.register(r"register", UserViewSet, basename="register")
# urlpatterns += router.urls