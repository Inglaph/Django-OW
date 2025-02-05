"""Vistas de la aplicación blog."""
from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import Post


def list_posts(request):
    """Listado de posts."""
    # traigo todos los posts de la base de datos
    posts = Post.objects.all()
    # renderizo la plantilla con los posts
    return render(request, 'post/list.html', {'posts': posts})


def post_detail(request, id):
    """Detalle de un post."""
    # traigo el post de la base de datos, o devuelvo 404 si no existe
    post = get_object_or_404(Post, id=id)
    # renderizo la plantilla con el post
    return render(request, 'post/detail.html', {'post': post})
