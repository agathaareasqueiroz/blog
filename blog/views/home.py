from django.shortcuts import render
from blog.models import Post

def home(request):

    # Obtém todos os `post`
    posts = Post.objects.all()

    # Passa as postagens para o template via `context`
    context = {
        'ownername': 'Joca da Silva',
        'posts': posts,
    }

    return render(request, 'home.html', context)