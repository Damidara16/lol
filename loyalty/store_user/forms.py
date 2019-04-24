from django import forms
from .models import Store

class UserCreation(forms.ModelForm):

    class Meta:
        model = Store
        fields = ()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=300, required=True)
    password = forms.CharField(max_length=300, widget = forms.PasswordInput(), required=True)
