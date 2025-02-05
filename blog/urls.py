from django.urls import path  # Importa la función path para definir rutas de URL
from . import views  # Importa las vistas desde el módulo actual

app_name = 'blog'

# creamos el patrón de URL para la vista list_posts
urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('int:<id>', views.post_detail, name='post_detail')
]
