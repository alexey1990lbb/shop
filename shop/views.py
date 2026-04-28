from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from .models import Category, Product


def home_view(request):
    # popular_products = Product.objects.filter(is_active=True).annotate(total_order=Sum('orderitem__quantity')).order_by(
    #     '-total_order')[:5]
    # if popular_products.count() < 5:
    #     extra = Product.objects.filter(is_active=True).exclude(
    #         id__in=[p.id for p in popular_products]
    #     ).order_by('-created_at')[:5 - popular_products.count()]
    #     from itertools import chain  # утилита для объединения списка
    #     popular_products = list(chain(popular_products, extra))

    promotions = Product.objects.filter(is_active=True, discount_percent__gt=0).order_by('-discount_percent')

    categories = Category.objects.filter(is_active=True)
    return render(request, 'shop/home.html',
                  {
                        # 'popular_products': popular_products,
                          'promotions': promotions,
                          'categories': categories,
                          'breadcrumbs': [{'title': 'Главная', 'url': '/'}]})


def category_list(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'shop/category_list.html', {
        'categories': categories,
        'breadcrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Категории', 'url': ''},
        ]
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = category.products.filter(is_active=True)
    return render(request, 'shop/product_list.html', {
        'category': category,
        'products': products,
        'breadcrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Категории', 'url': '/catalogue/categories/'},
            {'title': category.name, 'url': ''}
        ]
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(id=product.id)[:3]
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'related': related,
        'breadcrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Категории', 'url': '/catalogue/categories/'},
            {'title': product.category.name, 'url': product.category.get_absolute_url()},
            {'title': product.name, 'url': ''},
        ]
    })

def promotion_view(request):
    promotions = Product.objects.filter(is_active=True, discount_percent__gt=0).order_by('-discount_percent')
    return render(request, 'shop/promotions.html', {
        'promotions': promotions,
        'breadcrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Акции', 'url': ''},
        ]
    })