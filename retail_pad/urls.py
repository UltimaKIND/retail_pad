from retail_pad.apps import RetailPadConfig
from rest_framework.routers import DefaultRouter  # type: ignore
from retail_pad.views import NodeViewSet, ProductViewSet
from django.urls import path

app_name = RetailPadConfig.name

router = DefaultRouter()
router.register(r"retail_pad", NodeViewSet, basename="node")
router.register(r"product", ProductViewSet, basename="product")


urlpatterns = [] + router.urls
