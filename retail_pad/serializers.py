from rest_framework import serializers
from retail_pad.models import *

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'

class NodeSerializer(serializers.ModelSerializer):
    #contacts = serializers.IntegerField(source='contacts.first')
    contacts = ContactSerializer()

    class Meta:
        model = Node
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
