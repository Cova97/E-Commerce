from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        context = {'products': ['Telefonos', 'Carteras', 'Mochilas', 'Tenis']}
        return render(request, 'index.html', context)