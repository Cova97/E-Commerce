from django.shortcuts import render
from django.views import View

# Create your views here.
class Products(View):
    def get(sel, request):
        products = [] #TOOD: haz la query para traer products
        context = {'products': products}
        return render(request, 'products.html', context)