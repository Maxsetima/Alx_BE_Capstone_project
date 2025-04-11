from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, Product, Order, Logistics, Payment, Review

User = get_user_model()


#  Custom User Profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_picture']


#  User Serializer (for registration and details)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'role']

    def create(self, validated_data):
        # Ensure password is hashed when user is created
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#  Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    farmer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Automatically assign the current user as the farmer
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['farmer'] = request.user
        return super().create(validated_data)


#  Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    consumer = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['consumer'] = request.user
        return super().create(validated_data)


#  Logistics Serializer
class LogisticsSerializer(serializers.ModelSerializer):
    logistics_company = serializers.StringRelatedField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Logistics
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['logistics_company'] = request.user
        return super().create(validated_data)


#  Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    consumer = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['consumer'] = request.user
        return super().create(validated_data)
