from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderTrackingSerializer

class OrderTrackingView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderTrackingSerializer

# Create your views here.
