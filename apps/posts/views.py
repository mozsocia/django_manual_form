# views.py

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *  # You'll need to create a form for creating blogs

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('index')
    else:
        form = BlogForm()

    return render(request, 'blog/create.html', {'form': form})
