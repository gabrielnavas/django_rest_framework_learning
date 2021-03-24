from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', ProductViewSet, basename='products')


urlpatterns = router.urls