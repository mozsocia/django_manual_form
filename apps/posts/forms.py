# forms.py

from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'variations']
