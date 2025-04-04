class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'tracking_number', 'status']
