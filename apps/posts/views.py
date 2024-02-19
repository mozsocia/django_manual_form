# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Pass request.FILES for handling image upload
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('index')
    else:
        form = BlogForm()

    return render(request, 'blog/create.html', {'form': form})


def edit(request, blog_id):  # Define edit view
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('index')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/edit.html', {'form': form})