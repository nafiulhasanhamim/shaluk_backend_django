from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
urlpatterns = []

router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")
urlpatterns += router.urls