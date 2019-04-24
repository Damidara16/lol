from django import forms
from content.models import *

class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('store', 'total_sold')


class NOptionCreationForm(forms.ModelForm):
    class Meta:
        model = ParentNumOption
        exclude = ('store',)

class SOptionCreationForm(forms.ModelForm):
    class Meta:
        model = ParentSelectOption
        exclude = ('store',)
