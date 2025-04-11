from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'product', 'quantity']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'write_only': True}
        }
