from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import CustomUser
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, Logistics, Payment, Review
from .serializers import (
    UserSerializer, ProductSerializer, OrderSerializer,
    LogisticsSerializer, PaymentSerializer, ReviewSerializer
)

# API Home View
def home(request):
    return render(request, 'api/home.html')

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# User API
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # In a real scenario, you may use a custom registration serializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Product API
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order API
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Logistics API
class LogisticsListView(generics.ListAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer

class LogisticsCreateView(generics.CreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer

class LogisticsUpdateView(generics.UpdateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer

# Payment API
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Review API
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product__id=product_id)
