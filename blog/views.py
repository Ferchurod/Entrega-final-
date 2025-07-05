from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post
from django.views.generic import TemplateView


# Vista de inicio del blog
def inicio(request):
    return render(request, 'blog/inicio.html')

# Vista para crear un autor
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # O donde prefieras
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

# Vista para crear una categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

# Vista para crear un post
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # ¡Esto es clave!
            return redirect('inicio')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

# Vista para buscar posts
def buscar_post(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(titulo__icontains=query) if query else Post.objects.all()    
    return render(request, 'blog/buscar_post.html', {'posts': posts})

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'blog/page_list.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitulo', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitulo', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('page_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

    
    