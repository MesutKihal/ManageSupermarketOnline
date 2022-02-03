

from django import forms


class AddUser(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    firstname = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    lastname = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'input'}))
    confirm = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'input'}))

class LogUser(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'input'}))
    