from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CartAddProductForm, CartRemoveProductForm
from products.models import Product

def cart_add_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id))

    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if cart_item:
                cart_item['quantity'] += quantity
            else:
                cart[str(product_id)] = {'quantity': quantity}
            request.session['cart'] = cart
            messages.success(request, 'Product added to cart.')
            return redirect('products')
    else:
        form = CartAddProductForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'cart/add_product.html', context)

def cart_remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart_item = cart.get(str(product_id))

    if request.method == 'POST':
        form = CartRemoveProductForm(request.POST)
        if form.is_valid() and cart_item:
            del cart[str(product_id)]
            request.session['cart'] = cart
            messages.success(request, 'Product removed from cart.')
        return redirect('products')
    else:
        form = CartRemoveProductForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'cart/remove_product.html', context)
