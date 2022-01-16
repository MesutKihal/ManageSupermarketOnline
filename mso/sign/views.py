from django.shortcuts import render, redirect
from .forms import AddUser, LogUser
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages


def index(request):
    return render(request, 'sign/index.html')

def signup(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            if password == confirm:
                new = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                new.save()
                messages.success(request, "Account Created Successfully!")
            else:
                messages.error(request, "Passwords Don't match")
            return redirect("/signup")
    else:
        form = AddUser()
    return render(request, 'sign/signup.html', {'form':form})

def login(request):
    if request.method == "POST":
        form = LogUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authentication
            try:
                user = User.objects.get(username=username)
                if user.password != password:
                    messages.error(request,'Invalid password')
                    return redirect("/login")
            except User.DoesNotExist:
                user = None
            # If authentication is successful Login
            if user is not None:
                auth_login(request, user)
                # messages.info(request, f"{username} Logged In Successfully!")
                return redirect("owner-cashier")
            else:
                messages.error(request, "Cannot Logged In!")
                return redirect("/login")
    else:
        form = LogUser()
    return render(request, 'sign/login.html', {'form': form})

def logout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully!")
    return redirect("/login")
