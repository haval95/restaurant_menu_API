from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("menu-items", views.Menu_ItemView.as_view()),
    path("menu-items-fn", views.menu_items_fn_view),
    path("menu-items-djfl", views.Menu_Item_djfilters.as_view()),
    path("categories", views.CategoryView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("categories/<int:pk>", views.SingleCategoryView.as_view()),
    path("secret", views.secret),
    path("api-token-auth", obtain_auth_token),
    path("manager-view", views.manager_view)
]
