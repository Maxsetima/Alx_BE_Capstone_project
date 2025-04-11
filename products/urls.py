from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import path, include
from .views import OrderListCreateView, OrderTrackingView, PaymentListCreateView, ProductListCreateView, ProductUpdateDeleteView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls


urlpatterns = [

    path('', include(router.urls)),
    # Product API Endpoints
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductUpdateDeleteView.as_view(), name='product-detail'),

    # Order API Endpoints
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/tracking/', OrderTrackingView.as_view(), name='order-tracking'),

    # Payment API Endpoints
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
]
