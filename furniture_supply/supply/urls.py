from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('new/', views.order_create, name='order_create'),

    path('products/', views.product_list, name='product_list'),
    path('products/new/', views.product_create, name='product_create'),

    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/new/', views.supplier_create, name='supplier_create'),

    path('report/orders/', views.order_report, name='order_report'),
    path('report/products/', views.product_report, name='product_report'),
    path('report/suppliers/', views.supplier_report, name='supplier_report'),
]
