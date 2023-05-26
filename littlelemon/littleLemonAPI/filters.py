from .models import Menu_Item
from django_filters import rest_framework as filters



class MenuItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="item_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="item_price", lookup_expr='lte')
    category = filters.CharFilter(field_name="category__category_name", lookup_expr="exact")

    class Meta:
        model = Menu_Item
        fields = ['category__category_name', 'item_price']