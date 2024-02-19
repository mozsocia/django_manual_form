**Models**
```py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

**forms**
```py
from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category']

```

**urls**
```py
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('create/', create, name='create_blog'),
]

```


**views**
```py
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



```

```html
<form method="post" action="{% url 'create_blog' %}">
        {% csrf_token %}

        <label for="id_title">Title:</label>
        <input type="text" name="title" id="id_title" value="{{ form.title.value|default:'' }}" >
        {% if form.title.errors %}
            <span class="error">{{ form.title.errors.0 }}</span>
        {% endif %}

        <br>

        <label for="id_content">Content:</label>
        <textarea name="content" id="id_content" >{{ form.content.value|default:'' }}</textarea>
        {% if form.content.errors %}
            <span class="error">{{ form.content.errors.0 }}</span>
        {% endif %}

        <br>

        <label for="id_category">Category:</label>
        <select name="category" id="id_category" >
            {% for category_value, category_label in form.category.field.choices %}
                <option value="{{ category_value }}" 
                {% if form.category.value|stringformat:"s" == category_value|stringformat:"s" %}selected{% endif %}
                >
                    {{ category_label }}
                </option>
            {% endfor %}
        </select>
        {% if form.category.errors %}
            <span class="error">{{ form.category.errors.0 }}</span>
        {% endif %}

        <br>

        <button type="submit">Save</button>
    </form>

```
