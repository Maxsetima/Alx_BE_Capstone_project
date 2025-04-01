from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework.permissions import IsAuthenticated

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

class CartItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
from django.shortcuts import render

# Create your views here.
