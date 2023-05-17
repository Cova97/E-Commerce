from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            print("SIMON PERO NO QUIERO")
            form.save()
            messages.success(request, '¡Registro exitoso! Inicia sesión para continuar.')
            return redirect('login')
        else:
            print("NEL CARNAL")
            return render(request, 'accounts/register.html', {'form': form})
    form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, intenta nuevamente.')

    return render(request, 'index.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    return render(request, 'products')

