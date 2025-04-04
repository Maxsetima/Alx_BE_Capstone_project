from rest_framework.schemas import get_schema_view
from django.urls import path
from .views import (
    home,
    UserProfileView,
    # User API endpoints
    UserRegisterView, UserDetailView, UserUpdateView,
    # Product API endpoints
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    # Order API endpoints
    OrderCreateView, OrderDetailView, OrderUpdateView,
    # Logistics API endpoints
    LogisticsListView, LogisticsCreateView, LogisticsUpdateView,
    # Payment API endpoints
    PaymentCreateView, PaymentDetailView,
    # Review API endpoints
    ReviewCreateView, ReviewListView,
)

urlpatterns = [
    # API Home
    path('', home, name='api-home'),
    
     path('profile/', UserProfileView.as_view(), name='user-profile'),
    # User API endpoints
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('openapi/', get_schema_view(title="E-commerce API"), name='openapi-schema'),
    # Product API endpoints
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/new/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Order API endpoints
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),

    # Logistics API endpoints
    path('logistics/', LogisticsListView.as_view(), name='logistics-list'),
    path('logistics/new/', LogisticsCreateView.as_view(), name='logistics-create'),
    path('logistics/<int:pk>/update/', LogisticsUpdateView.as_view(), name='logistics-update'),

    # Payment API endpoints
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),

    # Review API endpoints
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:product_id>/', ReviewListView.as_view(), name='review-list'),
]
