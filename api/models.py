from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('consumer', 'Consumer'),
        ('logistics', 'Logistics'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='consumer')  # <- Add this line

    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",
        blank=True,
    )
    pass
    def __str__(self):
        return self.username

class Token(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.key
# Product Model (for Farmers)
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Livestock', 'Livestock'),
        ('Vegetables', 'Vegetables'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use dynamic reference

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
    consumer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.consumer.username}"


# Logistics Model
class Logistics(models.Model):
    STATUS_CHOICES = [
        ('In-transit', 'In-transit'),
        ('Delivered', 'Delivered'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='logistics')
    logistics_company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logistics')
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
    consumer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.consumer.username}"