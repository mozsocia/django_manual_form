from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    products = Product.objects.all()
    return render(request, 'prac.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
