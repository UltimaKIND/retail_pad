from rest_framework import serializers
from retail_pad.models import *
from retail_pad.validators import NodeValidator


class ContactSerializer(serializers.ModelSerializer):
    """
    сериализатор модели контактов
    """

    class Meta:
        model = Contacts
        exclude = ("node",)


class NodeSerializer(serializers.ModelSerializer):
    """
    сериализатор модели узла сети
    """

    contacts = ContactSerializer()

    class Meta:
        model = Node
        fields = "__all__"

    def create(self, validated_data):
        """
        создание объекта
        """
        node_data = {}
        node_data["name"] = validated_data.pop("name")
        node_data["supplier"] = validated_data.pop("supplier", None)
        node_data["duty_supp"] = validated_data.pop("duty_supp", None)
        if node_data["supplier"] and not node_data["duty_supp"]:
            node_data["duty_supp"] = 0
        if node_data["supplier"]:
            if node_data["supplier"].network_lvl != 0:
                node_data["network_lvl"] = 2
            else:
                node_data["network_lvl"] = 1
        else:
            node_data["network_lvl"] = 0
        contacts_data = validated_data.pop("contacts")
        node = Node.objects.create(**node_data)
        contacts_data["node"] = node
        contacts = Contacts.objects.create(**contacts_data)
        return node

    def validate(self, data):
        """
        валидация данных
        """
        NodeValidator()(data)
        return data


class ProductSerializer(serializers.ModelSerializer):
    """
    сериализатор модели продукта
    """

    class Meta:
        model = Product
        fields = "__all__"


class NodeDetailSerializer(serializers.ModelSerializer):
    """
    детальный сериализатор модели узла сети
    """

    contacts = ContactSerializer()
    products = ProductSerializer("products", many=True)

    class Meta:
        model = Node
        fields = "__all__"
