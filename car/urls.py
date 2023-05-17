from django.urls import path
from .views import cart_add_product, cart_remove_product

urlpatterns = [
    path('add/<int:product_id>/', cart_add_product, name='cart_add_product'),
    path('remove/<int:product_id>/', cart_remove_product, name='cart_remove_product'),
]
