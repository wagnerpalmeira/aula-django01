from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib import messages

def cadastrar_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        new_post = Post.objects.create(
            titulo=titulo,
            subtitulo=subtitulo
        )
        if new_post:
            messages.success(request, "Post criado com sucesso")


    return render(request, 'cadastrar_post.html')

def listar_posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'listar_posts.html', context)


def detalhe_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detalhe_post.html', {"post": post})
