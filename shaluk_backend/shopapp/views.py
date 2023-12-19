
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Shop
from .serializers import ShopSerializer
from rest_framework.response import Response
from rest_framework import status
from user import authentication
from rest_framework import views, response, exceptions, permissions

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'delete']:
            # Allow any user to perform GET requests
            return [AllowAny()]
        else:
            # Require authentication for POST, PUT, and DELETE requests
            
            # return [authentication.CustomUserAuthentication(), permissions.IsAuthenticated()]
            # return [IsAuthenticated()]
            return [AllowAny()]
    

    def get_queryset(self):
        shop_type = self.request.query_params.get('shop_type', None)
        if shop_type:
            return Shop.objects.filter(shop_type=shop_type)
        return Shop.objects.all()

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
         return Response({'message': 'Shop added successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)


    
    
    def update(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         instance = self.get_object()
         serializer = self.get_serializer(instance, data=request.data, partial=True)
         serializer.is_valid(raise_exception=True)
         self.perform_update(serializer)
         return Response({'message': 'Shop updated successfully'}, status=status.HTTP_200_OK)
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
    
        
