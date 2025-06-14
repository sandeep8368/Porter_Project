from rest_framework import serializers
from .models import DeliveryRequest

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = '__all__'
        read_only_fields = ['user', 'created_at']