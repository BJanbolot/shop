from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_product_list, name='product-list'),
    path('products/<str:product_slug>', views.get_product_detail, name='product-details'),
]