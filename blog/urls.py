# urls.py
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('create/', create, name='create_blog'),
    path('<int:blog_id>/edit/', edit, name='edit_blog'),

]
