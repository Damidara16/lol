from django.forms import forms
from .models import Store

class UserCreation(forms.ModelForm):

    class Meta:
        model = Store
        fields = ()
