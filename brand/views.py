from django.shortcuts import render
from .models import Category, Product


def main(request):
    category = Category.objects.filter(is_visible=True)
    return render(request, 'index.html')


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

