from django.urls import path
from apps.projects_management import views  

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  
    path('categories/<int:category_id>/', views.category_products, name='category_products'),  
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  
]
