from django.shortcuts import render
from .models import Products, Cashiers
from .forms import AddProduct, AddCashier
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'owner/index.html')
    
@login_required
def cashier(request):
    if request.method == "POST":
        form = AddCashier(request.POST)
        if form.is_valid():
            fullname_ = form.cleaned_data["fullname"]
            address_ = form.cleaned_data["address"]
            phone_number_ = form.cleaned_data["phone_number"]
            username_ = form.cleaned_data["username"]
            email_ = form.cleaned_data["email"]
            password_ = form.cleaned_data["password"]
            cashier = Cashiers(super=request.user,fullname=fullname_, address=address_, phone_number=phone_number_, username=username_, email=email_, password=password_)
            cashier.save()
    else:
        form = AddCashier()
    return render(request, 'owner/home.html', {'form':form})

@login_required
def about(request):
    return render(request, 'owner/about.html')

@login_required
def products(request):
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            barcode_ = form.cleaned_data["barcode"]
            title_ = form.cleaned_data["title"]
            type_ = form.cleaned_data["type"]
            price_ = form.cleaned_data["price"]
            quantity_ = form.cleaned_data["quantity"]
            description_ = form.cleaned_data["description"]
            product = Products(super=request.user, barcode=barcode_, title=title_, type=type_, price=price_, quantity=quantity_, description=description_)
            product.save()
    else:
        form = AddProduct()
    return render(request, 'owner/products.html', {'form':form})

@login_required
def sales(request):
    return render(request, 'owner/sales.html')

@login_required
def inventory(request):
    products = list(Products.objects.filter(super=request.user))
    context = {
        'products': products,
    }
    return render(request, 'owner/inventory.html', context)

@login_required
def settings(request):
    return render(request, 'owner/settings.html')
