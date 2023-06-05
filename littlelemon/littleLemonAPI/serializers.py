from rest_framework import serializers, validators
from .models import Category, Menu_Item
from decimal import Decimal
from rest_framework.validators import UniqueValidator



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ["id", "category_name"]
        
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name= "calculate_tax")
    #category = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
#     def validate_item_name(self, value):
#         return bleach.clean(value)
    

    
    item_name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Menu_Item.objects.all())]
    )
    def validate_item_price(self, value):
        if value < 2:
            raise serializers.ValidationError("price < 2")
    def validate(self, attrs):
        #attrs['item_name'] = bleach.clean(attrs['title'])
        if attrs["item_price"] < 2:
            raise serializers.ValidationError("price < 2")
        return super.validate(attrs)
    class Meta:
        model= Menu_Item
        fields = ["item_name", "item_ingridiants", "item_price", "image", "category", "category_id", "inventory", "price_after_tax"]
        extra_kwargs = {
            'item_price': {'min_value': 0},
            'inventory': {'min_value': 0},
            "item_name": {
                "validators": [
                    UniqueValidator(
                        queryset=Menu_Item.objects.all()
                    )
                ]
            }
        }

        

    def calculate_tax(self, product:Menu_Item):
        return product.item_price * Decimal(1.10)