from django.shortcuts import render
from django.views import View
from products.models import Product

# Create your views here.
class Car(View):
    def get(self, requesr):
        add = Product.objects.all()
        return render(requesr,'car.html',{'add':add})