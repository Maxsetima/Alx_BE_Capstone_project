from django.db import models
from api.models import CustomUser  # Ensure you import CustomUser
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Livestock', 'Livestock'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Grains', 'Grains'),
        ('Dairy', 'Dairy'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit (KES)")
    stock = models.IntegerField(default=0, help_text="Available stock units")
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(help_text="Quantity per unit (e.g. 10kg bag)")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Added choices for category
    farmer = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE, 
    related_name='products_products'  # Or 'marketplace_products', etc.
)
    image_url = models.URLField(blank=True, null=True)
    # created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
     # ✅ Add this Meta class here
    class Meta:
        ordering = ['-created_at']

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    
    tracking_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    consumer = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='product_orders'  # ✅ Added to avoid conflicts
    )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order #{self.order.pk}"
