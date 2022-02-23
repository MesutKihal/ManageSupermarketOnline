from django.shortcuts import render

def cash_register(request):
    return render(request, 'cashier/cash_register.html')
