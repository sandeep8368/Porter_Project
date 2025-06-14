from rest_framework import viewsets, permissions
from .models import DeliveryRequest
from .serializers import DeliverySerializer
# Create your views here.

class DeliveryView(viewsets.ModelViewSet):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
