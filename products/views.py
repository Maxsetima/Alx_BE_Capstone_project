from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, Payment
from .serializers import ProductSerializer, OrderSerializer, PaymentSerializer, OrderTrackingSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    """
    View to list all products or create a new product (for farmers only).
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can add products

    def perform_create(self, serializer):
        # Automatically associate the logged-in user as the farmer for the product
        serializer.save(farmer=self.request.user)

class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update/delete

# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    """
    View to list all orders for the authenticated user and create a new order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter orders by the logged-in user
        return Order.objects.filter(consumer=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user as the consumer of the order
        serializer.save(consumer=self.request.user)

class OrderTrackingView(generics.RetrieveAPIView):
    """
    View to retrieve tracking information for a specific order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderTrackingSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view the order tracking

# Payment Views
class PaymentListCreateView(generics.ListCreateAPIView):
    """
    View to list all payments or create a new payment.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can view/create payments

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the payment
        serializer.save(order__consumer=self.request.user)

