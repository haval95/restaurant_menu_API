from rest_framework import generics
from .models import Menu_Item, Category
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .filters import  MenuItemFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(["GET"])
def menu_items_fn_view(request):
    if request.method == "GET":
        items = Menu_Item.objects.select_related("category").all()
        category_name = request.query_params.get("category")
        to_price = request.query_params.get("to_price")
        search = request.query_params.get("search")
        ordering = request.query_params.get("ordering")
        perpage = request.query_params.get("perpage", default=2)
        page = request.query_params.get("page", default=1)
        if category_name:
            items = items.filter(category__category_name=category_name)
        if to_price:
            items = items.filter(item_price__lte= to_price)
        if search:
            items = items.filter(item_name__icontains= search)
        if ordering:
            ordering_feilds = ordering.split(",")
            items = items.order_by(*ordering_feilds)
        
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    
    
class Menu_ItemView(generics.ListCreateAPIView):
    queryset = Menu_Item.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get("category")
        to_price = self.request.query_params.get("to_price")
        search = self.request.query_params.get("search")
        ordering = self.request.query_params.get("ordering")

        if category_name:
            queryset = queryset.filter(category__category_name=category_name)
        if to_price:
            queryset = queryset.filter(item_price__lte=to_price)
        if search:
            queryset = queryset.filter(item_name__icontains=search)
        if ordering:
            ordering_feilds = ordering.split(",")
            queryset = queryset.order_by(*ordering_feilds)

        return queryset

class Menu_Item_djfilters(generics.ListCreateAPIView):
    queryset = Menu_Item.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    
    filterset_class = MenuItemFilter
    filterset_fields = ('category', 'item_price')
    ordering_fields = ['item_price', 'inventory']
    search_fields = ['item_name', "category__category_name"]
    
        
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu_Item.objects.all()
    serializer_class = MenuItemSerializer
    
        

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


class SingleCategoryView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "some secre msg"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "only manager sees this part"})
    else:
        return Response({"message": "you are not authorized"}, 403)
