from django.shortcuts import render
from django.views import View
from products.models import Product

# Create your views here.
class Products(View):
    def get(sel, request):
        products = Product.objects.all() #TOOD: haz la query para traer products
        context = {'products': products}
        return render(request, 'products.html', context)