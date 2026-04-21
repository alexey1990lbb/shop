from django.urls import path
from . import views

app_name = 'shop' # shop:home

urlpatterns = [
    path('', views.home_view, name='home'),
    path('categories/', views.category_list, name='category-list'),
    path('categories/<slug:slug>/', views.category_detail, name='category-detail'),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
    path('promotions/', views.promotion_view, name='promotion-list'),
]