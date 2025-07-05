from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, blank=True, null=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True) 
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='pages/')
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title