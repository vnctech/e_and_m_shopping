from django.shortcuts import render, get_object_or_404
from apps.projects_management.models import Product, Category



def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def product_list(request):
    products = Product.objects.all()  
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)  
