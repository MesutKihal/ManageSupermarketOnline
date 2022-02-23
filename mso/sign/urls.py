from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/owner/', views.login_as_owner, name="login-owner"),
    path('login/cashier/', views.login_as_cashier, name="login-cashier"),
    path('logout/', auth_views.LogoutView.as_view(template_name="sign/logout.html"), name="logout"),
    path('signup/', views.signup, name="signup"),
]
