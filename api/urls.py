from django.contrib import admin
from django.urls import path, include
from .views import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Correct import after installation
from .views import (
    APIHomeView,  # Newly added API home view
    UserRegisterView, UserDetailView, UserUpdateView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    OrderCreateView, OrderDetailView, OrderUpdateView,
    LogisticsListView, LogisticsCreateView, LogisticsUpdateView,
    PaymentCreateView, PaymentDetailView,
    ReviewCreateView, ReviewListView,
    product_list, order_list, payment_list  # Import your views
)

urlpatterns = [
    # API Home
    path('', APIHomeView.as_view(), name='api-home'),

    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),

    path('api-token-auth/', obtain_auth_token),  # Token generation endpoint
    # User API endpoints
    path('auth/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),

    # Product API endpoints (remove duplicate function-based view)
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Order API endpoints
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),

    # Optional: If you want to keep the function-based order list (but NOT duplicate)
    path('orders/list/', order_list, name='order-list'),

    # Logistics API endpoints
    path('logistics/', LogisticsListView.as_view(), name='logistics-list'),
    path('logistics/new/', LogisticsCreateView.as_view(), name='logistics-create'),
    path('logistics/<int:pk>/update/', LogisticsUpdateView.as_view(), name='logistics-update'),

    # Payment API endpoints
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),

    # Optional: Separate endpoint for listing payments via function view
    path('payments/list/', payment_list, name='payment-list'),

    # Review API endpoints
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/product/<int:product_id>/', ReviewListView.as_view(), name='review-list'),
]
