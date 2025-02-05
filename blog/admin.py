"""Configuración del panel de administración de Django para el modelo Post."""
from django.contrib import admin
from .models import Post

# admin.site.register(Post)

# Decorador que se utiliza para registrar el modelo en el panel de administración de Django.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Configuracion admin de Django para el modelo Post."""
    list_display = ['title', 'slug', 'created_at', 'published']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



    # title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, unique=True)
    # content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # published = models.BooleanField(default=False)
