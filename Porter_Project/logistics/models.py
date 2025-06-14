from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DeliveryRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_address = models.CharField(max_length=255)
    drop_address = models.CharField(max_length=255)
    item_description = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Picked', 'Picked'),
        ('Delivered', 'Delivered'),
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"