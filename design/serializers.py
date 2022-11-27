from .models import Design_Model, Item_Model

from rest_framework import serializers

class Design_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Design_Model
        fields = "__all__"

class Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Model
        fields = "__all__"