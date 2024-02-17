# views.py

from django.shortcuts import render, redirect, get_object_or_404
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



def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('your_app_name:index')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'your_app_name/edit.html', {'form': form, 'blog': blog})