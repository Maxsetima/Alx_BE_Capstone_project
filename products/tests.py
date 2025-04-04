from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Order, Product

User = get_user_model()

class OrderTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)
        
        # Create test users
        self.farmer = User.objects.create_user(username="farmer1", password="password123")
        self.consumer = User.objects.create_user(username="consumer1", password="password123")

        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.99,
            quantity=5,
            category="Vegetables",
            farmer=self.farmer  # Ensure farmer exists
        )

        self.order = Order.objects.create(
            product=self.product,
            consumer=self.consumer,  # Ensure consumer exists
            quantity=2,
            total_price=21.98,
            status='Pending'  # Ensure this matches Order model
        )

    def test_order_tracking(self):
        """Test if an order is created correctly"""
        self.assertEqual(self.order.status, 'Pending')
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.total_price, 21.98)


    def test_order_tracking(self):
        response = self.client.get(f'/api/order-tracking/{self.order.id}/')
        self.assertEqual(response.status_code, 200)

    def test_order_tracking(self):
        """Test order tracking updates correctly."""
        self.order.status = "Shipped"
        self.order.save()

        updated_order = Order.objects.get(pk=self.order.pk)
        self.assertEqual(updated_order.status, "Shipped")
# Create your tests here.
