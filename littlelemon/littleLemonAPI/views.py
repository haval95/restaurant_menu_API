from rest_framework import generics
from .models import Menu_Item, Category
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def menu_items_fn_view(request):
    if request.method == "GET":
        items = Menu_Item.objects.select_related("category").all()
        category_name = request.query_params.get("category")
        to_price = request.query_params.get("to_price")
        search = request.query_params.get("search")
        if category_name:
            items = items.filter(category__category_name=category_name)
        if to_price:
            items = items.filter(item_price__lte= to_price)
        if search:
            items = items.filter(item_name__icontains= search)
        
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
        
        

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


class SingleCategoryView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Menu_ItemView(generics.ListCreateAPIView):
    queryset = Menu_Item.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    def filter_queryset(self, queryset):
        category_name = self.request.query_params.get("category")
        to_price = self.request.query_params.get("to_price")
        search = self.request.query_params.get("search")
        if category_name:
            queryset = queryset.filter(category__category_name=category_name)
        if to_price:
            queryset = queryset.filter(item_price__lte=to_price)
        if search:
            queryset = queryset.filter(item_name__icontains=search)
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu_Item.objects.all()
    serializer_class = MenuItemSerializer