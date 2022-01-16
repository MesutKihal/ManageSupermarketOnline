from django.urls import path, include
from . import views

urlpatterns = [
    path('cashier/', views.cashier, name="owner-cashier"),
    path('about/', views.about, name="owner-about"),
    path('products/', views.products, name="owner-products"),
    path('sales/', views.sales, name="owner-sales"),
    path('inventory/', views.inventory, name="owner-inventory"),
    path('settings/', views.settings, name="owner-settings"),
]
