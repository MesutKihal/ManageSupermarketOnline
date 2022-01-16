

from django import forms


class AddUser(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'log-entry'}))
    firstname = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'log-entry'}))
    lastname = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'log-entry'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'log-entry'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'id': 'log-entry'}))
    confirm = forms.CharField(label="", widget=forms.PasswordInput(attrs={'id': 'log-entry'}))

class LogUser(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'log-entry'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'id': 'log-entry'}))
    