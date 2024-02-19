# forms.py
from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'image', 'is_active']  # Added 'image' and 'is_active' fields

