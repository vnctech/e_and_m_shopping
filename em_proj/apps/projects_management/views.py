from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Subcategory

def product_list(request):
    categories = Category.objects.all()  
    subcategories = Subcategory.objects.all()  
    products = Product.objects.all()  
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
    }
    return render(request, 'list_view.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    context = {
        'product': product,
    }
    return render(request, 'detail_view.html', context)