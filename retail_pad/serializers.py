from rest_framework import serializers
from retail_pad.models import *

class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
