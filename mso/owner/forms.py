
from django import forms


class AddProduct(forms.Form):
    barcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    title = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    type = forms.CharField(max_length=100, label="",  widget=forms.TextInput(attrs={'id': 'entry'}))
    price = forms.FloatField(label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    quantity = forms.IntegerField(label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    description = forms.CharField(max_length=200, label="", widget=forms.TextInput(attrs={'id': 'entry'}))

class AddCashier(forms.Form):
    fullname = forms.CharField(max_length=50,  label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    address = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    phone_number = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    username = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'id': 'entry'}))
    password = forms.CharField(max_length=100, label="", widget=forms.PasswordInput(attrs={'id': 'entry'}))
