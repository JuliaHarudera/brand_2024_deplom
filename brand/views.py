from django.shortcuts import render
from .models import Category, Product


def main(request):
    categories = Category.objects.filter(is_visible=True)
    context = {'categories': categories}
    return render(request, 'brand_main.html', context=context)


def category_detail(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {'products': products}
    return render(request, 'products.html', context=context)





