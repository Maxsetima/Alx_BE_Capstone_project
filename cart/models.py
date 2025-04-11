from django.db import models
from django.conf import settings
from django.apps import apps  # Import the Product model from the products app

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Ensures user model is used dynamically
        on_delete=models.CASCADE,
        related_name='cart_items'  # Allows easy access to the user's cart items
    )
    product = models.ForeignKey(
        'products.Product',  # Reference to the Product model in the 'products' app
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)  # Default to 1, assuming user can add at least one item

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"  # Custom string representation for easier debugging
