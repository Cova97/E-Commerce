from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import ProductCreate

# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.all() 
        context = {'products': products}
        return render(request, 'products/products.html', context)

class CreateProduct(View):
    def get(self, request):
        form = ProductCreate()
        context = {'form': form}
        return render(request, 'products/form.html', context)
    
    def post(self, request):
        form = ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print('ERROR')
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/products.html', context)

class UpdateProduct(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(instance=product)
        context = {'form': form}
        return render(request, 'products/update_form.html', context)
    
    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print('ERROR')
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/update_form.html', context)

class DeleteProduct(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'products/delete_form.html', context)

    def post(self, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('products')
