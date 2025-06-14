from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryView


router = DefaultRouter()
router.register(r'deliveries', DeliveryView)


urlpatterns = [
    path('', include(router.urls)),
]
