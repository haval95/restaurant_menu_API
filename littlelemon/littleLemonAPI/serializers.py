from rest_framework import serializers 
from .models import Category, Menu_Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= "__all__"
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Menu_Item
        fields = "__all__"
        
