from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Adiciona as URLS de 'blog' ao projeto
    path('', include('blog.urls')),
]
