from rest_framework import viewsets
from rest_framework.response import Response
from retail_pad.serializers import *
from rest_framework.filters import SearchFilter
from users.permissions import IsActiveUser


class NodeViewSet(viewsets.ModelViewSet):
    """
    контроллер Node
    """

    queryset = Node.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [SearchFilter]
    search_fields = ["contacts__country"]

    def get_serializer_class(self):
        """
        для детального просмотра - расширенный сериализатор
        """
        if self.action == "retrieve":
            return NodeDetailSerializer
        else:
            return NodeSerializer

    def update(self, request, *args, **kwargs):
        """
        запрет на обновление поля задолженность перед поставщиком, и самого поставщика
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if "duty_supp" in serializer.validated_data:
            serializer.validated_data.pop("supplier")
            serializer.validated_data.pop("duty_supp")
        self.perform_update(serializer)

        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    """
    контроллер Product
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()