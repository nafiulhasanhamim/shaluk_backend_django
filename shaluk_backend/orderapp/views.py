
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Order
from user.models import User
from .serializers import OrderSerializer, UserOrderSerializer
from rest_framework.response import Response
from rest_framework import status
from user import authentication
from django.shortcuts import get_object_or_404

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Allow any user to perform GET requests
            return [AllowAny()]
        else:
            # Require authentication for POST, PUT, and DELETE requests
            return [AllowAny()]

    # def get_queryset(self):
    #     user_id = self.request.query_params.get('user_id', None)
    #     if user_id:
    #         return Order.objects.filter(user__id=user_id)
    #     return Order.objects.all()
    
    def list(self, request, *args, **kwargs):
        # Custom logic for listing all shops
        user_email = self.request.query_params.get('user_email', None)
        if user_email is None:
           user = authentication.CustomUserAuthentication2.authenticate(self, request)
           if user is not None and user["user"] is not None and user["is_superuser"] == True:
            orders = self.get_queryset()
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
           else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)
        else:
        #    return Response({'msg': 'user'})
           if user_email:
              orders = (Order.objects.filter(user__email=user_email))
              serializer = UserOrderSerializer(orders, many=True)
              return Response(serializer.data, status=status.HTTP_200_OK)
              

            #   return Response({'orders': orders})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        # user = authentication.CustomUserAuthentication2.authenticate(self, request)
        # if user is not None and user["user"] is not None and user["is_superuser"] == False:
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         self.perform_create(serializer)
         return Response({'message': 'Order is placed successfully!'}, status=status.HTTP_201_CREATED)
        # else:
            # return Response({'message': 'Please login first'}, status=status.HTTP_200_OK)
    

    def update(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         instance = self.get_object()
         serializer = self.get_serializer(instance, data=request.data, partial=True)
         serializer.is_valid(raise_exception=True)
         self.perform_update(serializer)
         return Response({'message': 'Order is update successfully'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)

    
    def destroy(self, request, *args, **kwargs):
        user = authentication.CustomUserAuthentication2.authenticate(self, request)
        if user is not None and user["user"] is not None and user["is_superuser"] == True:
         instance = self.get_object()
         self.perform_destroy(instance)
         return Response({'message': 'Order deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You dont have access'}, status=status.HTTP_200_OK)


