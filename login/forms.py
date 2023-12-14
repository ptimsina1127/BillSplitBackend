from django import forms
from .models import Item
class itemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["itemName","itemPrice","itemCategory"]