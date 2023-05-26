from rest_framework import serializers 
from .models import Category, Menu_Item
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= "__all__"
        
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name= "calculate_tax")
    class Meta:
        model= Menu_Item
        fields = ["item_name", "item_ingridiants", "item_price", "image", "category_id", "inventory", "price_after_tax"]
        

    def calculate_tax(self, product:Menu_Item):
        return product.item_price * Decimal(1.10)