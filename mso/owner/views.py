from django.shortcuts import render, redirect
from .models import Products, Cashiers
from .forms import AddProduct, AddCashier, ChangeUsername, ChangePassword
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt

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
            return redirect("/cashier")
    else:
        form = AddCashier()
    return render(request, 'owner/cashier.html', {'form':form})

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
            return redirect("/products")
    else:
        form = AddProduct()
    return render(request, 'owner/products.html', {'form':form})

@login_required
def sales(request):
    plt.style.use("fivethirtyeight")
    plt.plot([i for i in range(1, 20)], [i for i in range(1, 20)])
    
    plt.title('Sales Per Day')
    plt.ylabel('Soled Products')
    plt.xlabel('Days')
    plt.autoscale()
    plt.savefig("owner/static/img/plot.png")
    
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
    
@login_required
def change_username(request):
    if request.method == "POST":
       form = ChangeUsername(request.POST)
       if form.is_valid():
          username_ = form.cleaned_data["username"]
          request.user.username = username_
          request.user.save()
          return redirect("/owner/settings")
    else:
        form = ChangeUsername()
    return render(request, 'owner/change_username.html', {'form':form})
    
        
@login_required
def change_password(request):    
    if request.method == "POST":
        form = ChangePassword(request.POST)
        if form.is_valid():
            newpassword_ = form.cleaned_data["newpassword"]
            confirmnew_ = form.cleaned_data["confirmnew"]
            if newpassword_ == confirmnew_:               
                request.user.password = newpassword_
                request.user.save()
                return redirect("/owner/settings")
            else:
                messages.error(request, "Passwords Don't match")
                return redirect("/owner/settings/change_password")
    else:
        form = ChangePassword()
    return render(request, 'owner/change_password.html', {'form':form})
    
@login_required
def manage_cashiers(request):
    cashiers = list(Cashiers.objects.filter(super=request.user))
    context = {
        'cashiers': cashiers,
    }
    return render(request, 'owner/manage_cashiers.html', context)