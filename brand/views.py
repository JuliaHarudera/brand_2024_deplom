from django.shortcuts import render
from .models import Category, Product


def main(request):
    category = Category.objects.filter(is_visible=True)
    return render(request, 'index.html')

