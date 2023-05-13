from django.shortcuts import render, redirect
from django.views import View
from .models import Account
from .forms import AccountCreate
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class Accounts(View):
    def get(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('products')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/accounts.html', {'form': form})

class CreateAccount(View):
    def get(self,request):
        form = AccountCreate()
        context = {'form':form}
        return render(request, 'accounts/accounts.html', context)


