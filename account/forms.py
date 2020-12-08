from django import forms


class LoginForm(forms.Form):
    """TODO docstring"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
