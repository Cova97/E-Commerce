from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    #email = forms.EmailField(max_length=255, help_text='Requerido. Proporciona una dirección de correo electrónico válida.')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

