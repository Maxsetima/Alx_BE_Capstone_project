from django.urls import path, include
from .views import CartItemListCreateView, CartItemUpdateDeleteView
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'items', CartItemViewSet)


urlpatterns = [
    path('items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('items/<int:pk>/', CartItemUpdateDeleteView.as_view(), name='cart-item-update-delete'),
    path('', include(router.urls)),
]
