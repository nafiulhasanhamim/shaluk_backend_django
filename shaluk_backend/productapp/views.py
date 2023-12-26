
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from user import authentication

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Allow any user to perform GET requests
            return [AllowAny()]
        else:
            # Require authentication for POST, PUT, and DELETE requests
            return [AllowAny()]

    def get_queryset(self):
        shop_type = self.request.query_params.get('shop_type', None)
        shop_name = self.request.query_params.get('shop_name', None)
        if shop_type:
            return Product.objects.filter(shop__shop_type=shop_type)
        elif shop_name:
           return Product.objects.filter(shop__shop_name=shop_name)
           
        return Product.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         self.perform_create(serializer)
         return Response({'message': 'Product added successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)
    

    def update(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         instance = self.get_object()
         serializer = self.get_serializer(instance, data=request.data, partial=True)
         serializer.is_valid(raise_exception=True)
         self.perform_update(serializer)
         return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)

    
    def destroy(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         instance = self.get_object()
         self.perform_destroy(instance)
         return Response({'message': 'Shop deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)


