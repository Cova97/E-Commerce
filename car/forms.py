from django import forms
from .models import Product

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class CartRemoveProductForm(forms.Form):
    pass
