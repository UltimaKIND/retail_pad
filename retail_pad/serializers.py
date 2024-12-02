from rest_framework import serializers
from retail_pad.models import *

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        exclude = ('node',)

class NodeSerializer(serializers.ModelSerializer):
    #contacts = serializers.IntegerField(source='contacts.first')
    contacts = ContactSerializer()

    class Meta:
        model = Node
        fields = '__all__'

    def create(self, validated_data):
        node_data = {}
        node_data['name'] = validated_data.pop('name')
        node_data['supplier'] = validated_data.pop('supplier', None)
        node_data['duty_supp'] = validated_data.pop('duty_supp', None)
        contacts_data = validated_data.pop('contacts')
        node = Node.objects.create(**node_data)
        contacts_data['node'] = node
        contacts = Contacts.objects.create(**contacts_data)
        return node


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
