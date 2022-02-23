from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cash_register, name="cashier-cash_register"),
]
