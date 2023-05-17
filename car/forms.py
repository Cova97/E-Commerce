from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class CartRemoveProductForm(forms.Form):
    pass
