# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_product, name='create_product'),
]
