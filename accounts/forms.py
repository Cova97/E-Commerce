from django import forms
from .models import Account

class AccountCreate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = '__all__'