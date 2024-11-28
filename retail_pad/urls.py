from retail_pad.apps import RetailPadConfig
from rest_framework.routers import DefaultRouter  # type: ignore
from retail_pad.views import NodeViewSet
from django.urls import path

app_name = RetailPadConfig.name

router = DefaultRouter()
router.register(r'', NodeViewSet, basename='node')

urlpatterns = [
] + router.urls