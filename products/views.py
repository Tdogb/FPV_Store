from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by('date_released')
    return render(request, 'products/product_list.html', {'products': products})

def product_page(request, slug):
    products = Product.objects.get(slug=slug)
    return render(request, 'products/product_page.html', {'products': products})