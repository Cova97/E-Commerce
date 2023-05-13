from django.urls import path
from .views import *

urlpatterns = [
    path('', Accounts.as_view(), name='accounts')
]