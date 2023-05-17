from django.urls import path
from .views import cart_add_product, cart_remove_product, car, clean

urlpatterns = [
    path('add/<int:id>/', cart_add_product, name='cart_add_product'),
    path('remove/<int:id>/', cart_remove_product, name='cart_remove_product'),
    path('cart/', car, name='carrito'),
    path('clean/', clean, name='limpiar'),
]
