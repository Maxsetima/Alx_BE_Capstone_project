from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Payment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser, Product, Order, Logistics, Payment, Review
from .serializers import (
    UserSerializer, UserProfileSerializer, ProductSerializer, 
    OrderSerializer, LogisticsSerializer, PaymentSerializer, ReviewSerializer
)

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def your_view(request):
    # Your view code here
    data = {
        "message": "This is a protected endpoint."
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    products = Product.objects.all()
    return Response(products)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()  # Replace with actual logic to retrieve orders
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    return Response({"orders": orders}, status=status.HTTP_200_OK)

@api_view(['GET'])
def payment_list(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


# API Home View
def home(request):
    return render(request, 'api/home.html')
class APIHomeView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})


# User Profile API
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensures the profile of the currently authenticated user is returned
        return self.request.user


# User API
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow public access to registration endpoint

    def perform_create(self, serializer):
        # Here you can do custom actions like sending a welcome email or other post-registration tasks.
        serializer.save()


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to view details


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can update their info

    def get_object(self):
        # Updates the current user's data only
        return self.request.user


# Product API
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Require authentication to view the products


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create products


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update products


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete products


# Order API
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create orders


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view order details


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update orders


# Logistics API
class LogisticsListView(generics.ListAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
    permission_classes = [IsAuthenticated]  # Require authentication to view logistics


class LogisticsCreateView(generics.CreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create logistics


class LogisticsUpdateView(generics.UpdateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update logistics


# Payment API
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create payment entries


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view payment details


# Review API
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create reviews


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view reviews

    def get_queryset(self):
        # Fetch reviews related to a particular product
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product__id=product_id)