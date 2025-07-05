from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Categoria, Post

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)
from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categoria']

from django.contrib import admin
from .models import Page

admin.site.register(Page)
