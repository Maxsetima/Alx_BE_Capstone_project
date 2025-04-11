from rest_framework import serializers
from .models import Order, Payment, Product

class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'tracking_number', 'status']  # Basic fields for tracking an order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # You can specify the exact fields you want here if necessary

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Includes all fields for Payment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Includes all fields for Product
        read_only_fields = ['farmer', 'created_date']  # These fields can't be modified after creation
