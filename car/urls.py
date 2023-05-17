from django.urls import path
from .views import cart_add_product, cart_remove_product, car

urlpatterns = [
    path('add/<int:id>/', cart_add_product, name='cart_add_product'),
    path('remove/<int:id>/', cart_remove_product, name='cart_remove_product'),
    path('car/', car, name='carrito')
]
