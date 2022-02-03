
from django import forms


class AddProduct(forms.Form):
    barcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    title = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class': 'input'}))
    type = forms.CharField(max_length=100, label="",  widget=forms.TextInput(attrs={'class': 'input'}))
    price = forms.FloatField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    quantity = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(max_length=200, label="", widget=forms.TextInput(attrs={'class': 'input'}))

class AddCashier(forms.Form):
    fullname = forms.CharField(max_length=50,  label="", widget=forms.TextInput(attrs={'class': 'input'}))
    address = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'input'}))
    phone_number = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'input'}))
    username = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'class': 'input'}))

class ChangeUsername(forms.Form):
    username = forms.CharField(max_length=50,  label="", widget=forms.TextInput(attrs={'class': 'input'}))
    
class ChangePassword(forms.Form):
    newpassword = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'class': 'input'}))
    confirmnew = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'class': 'input'}))
