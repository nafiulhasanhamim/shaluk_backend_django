# # urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ShopViewSet

# router = DefaultRouter()
# router.register(r'shops', ShopViewSet, basename='shop')

# urlpatterns = [
#     path('addshop/', include(router.urls)),
# ]


# authapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet

router = DefaultRouter()
urlpatterns = [
    
]


router = DefaultRouter()
router.register(r"shop", ShopViewSet, basename="shop")
urlpatterns += router.urls