
from django.contrib import admin
from django.urls import path
from posts.views import listar_posts, detalhe_post, cadastrar_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', listar_posts),
    path('posts/<int:id>/', detalhe_post),
    path('posts/cadastrar/', cadastrar_post)
]
