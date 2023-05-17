from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CartAddProductForm, CartRemoveProductForm
from .models import Product

def cart_add_product(request, id):
    product = get_object_or_404(Product, id=id)
    car = request.session.get('car', {})
    cart_item = car.get(id)

    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if cart_item:
                cart_item['quantity'] += quantity
            else:
                car[id] = {'quantity': quantity}
            request.session['car'] = car
            messages.success(request, 'Producto agregado el carrito')
            return redirect('carrito')
    else:
        form = CartAddProductForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'car/add_product.html', context)

def cart_remove_product(request, id):
    product = get_object_or_404(Product, id=id)
    car = request.session.get('car', {})
    cart_item = car.get(id)

    if request.method == 'POST':
        form = CartRemoveProductForm(request.POST)
        if form.is_valid() and cart_item:
            del car[id]
            request.session['car'] = car
            messages.success(request, 'Producto eliminado del carrito')
        return redirect('carrito')
    else:
        form = CartRemoveProductForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'car/remove_product.html', context)

def car(request):
    car = request.session.get('car', {})
    products = Product.objects.filter(id__in=car.keys())
    context = {
        'products': products
        }
    return render(request, 'car/car.html', context)



