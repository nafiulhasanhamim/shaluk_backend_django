from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
urlpatterns = []

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")
urlpatterns += router.urls