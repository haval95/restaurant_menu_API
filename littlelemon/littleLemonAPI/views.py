from rest_framework import generics
from .models import Menu_Item, Category
from .serializers import CategorySerializer, MenuItemSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


class SingleCategoryView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Menu_ItemView(generics.ListCreateAPIView):
    queryset = Menu_Item.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu_Item.objects.all()
    serializer_class = MenuItemSerializer