from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """Отображает список всех товаров."""
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    """Отображает детальную информацию о товаре."""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})