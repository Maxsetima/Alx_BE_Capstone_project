from django.urls import path
from .views import CartItemListCreateView, CartItemUpdateDeleteView

urlpatterns = [
    path('items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('items/<int:pk>/', CartItemUpdateDeleteView.as_view(), name='cart-item-update-delete'),
]
