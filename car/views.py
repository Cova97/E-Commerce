from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

carrito = []# guarndan los datos en la lista

def cart_add_product(request, id):
    product = get_object_or_404(Product, id=id)
    print(f"Añadiste al carrito {product}") 
    #Disminuimos el stock
    product.stock = product.stock - 1
    product.save()
    #Añadimos al carrito
    carrito.append(product)
    print(carrito)
    return redirect('home')

def cart_remove_product(request, id):
    product = get_object_or_404(Product, id=id)
    #Verify if exist product in carrito
    if product in carrito:
        #Remove product from carrito
        carrito.remove(product)
        #Update product stock
        product.stock = product.stock + 1
        product.save()

    return redirect('carrito')

def car(request):
    context = {
        'cart': carrito
        }
    return render(request, 'car/car.html', context)

def clean(request):
    carrito.clear()
    return redirect('home')



