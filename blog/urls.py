from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    # Vistas normales
    path('', views.inicio, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),

    # CBV para pages
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/update/', PageUpdateView.as_view(), name='page_update'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)