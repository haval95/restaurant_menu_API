from rest_framework import serializers 
from .models import Category, Menu_Item
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ["id", "category_name"]
        
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name= "calculate_tax")
    #category = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model= Menu_Item
        fields = ["item_name", "item_ingridiants", "item_price", "image", "category", "category_id", "inventory", "price_after_tax"]
        extra_kwargs = {
            'item_price': {'min_value': 0},
            'inventory': {'min_value': 0}
        }
        

    def calculate_tax(self, product:Menu_Item):
        return product.item_price * Decimal(1.10)