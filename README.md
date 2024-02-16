**Models**
```py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
```

**forms**
```py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

**urls**
```py
# urls.py
from django.urls import path
from .views import post_index, post_create, post_store, post_show, post_edit, post_update, post_destroy

urlpatterns = [
    # Read All
    path('posts/', post_index, name='post-index'),

    # Create
    path('posts/create/', post_create, name='post-create'),
    path('posts/store/', post_store, name='post-store'),

    # Read one
    path('posts/<int:post_id>/', post_show, name='post-show'),

    # Update
    path('posts/<int:post_id>/edit/', post_edit, name='post-edit'),
    path('posts/<int:post_id>/update/', post_update, name='post-update'),

    # Delete
    path('posts/<int:post_id>/destroy/', post_destroy, name='post-destroy'),
]

```


**views**
```py
# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import PostForm
from .models import Post

@require_GET
def post_index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

@require_GET
def post_create(request):
    form = PostForm()
    return render(request, 'create.html', {'form': form})

@require_POST
def post_store(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('post-show', post_id=post.id)
    return render(request, 'create.html', {'form': form})

@require_GET
def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'show.html', {'post': post})

@require_GET
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form, 'post': post})

@require_http_methods(["PUT", "PATCH"])
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post-show', post_id=post.id)
    return render(request, 'edit.html', {'form': form, 'post': post})

@require_http_methods(["DELETE"])
def post_destroy(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post-index')
```
