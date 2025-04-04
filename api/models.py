from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",  # Add a unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # Add a unique related_name
        blank=True,
    )


# Product Model (for Farmers)
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Livestock', 'Livestock'),
        ('Vegetables', 'Vegetables'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # Changed related_name from 'products' to 'api_products'
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_products')
    image = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Order Model (for Consumers)
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

# Logistics Model
class Logistics(models.Model):
    STATUS_CHOICES = [
        ('In-transit', 'In-transit'),
        ('Delivered', 'Delivered'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='logistics')
    logistics_company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logistics')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In-transit')
    shipment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Logistics for Order #{self.order.pk}"

# Payment Model
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

# Review Model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    consumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.consumer.username}"

