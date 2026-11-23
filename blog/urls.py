# blog\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                              # Rota para página inicial
    path('contacts/', views.contacts, name='contacts'),             # Rota para a página de contatos
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Página do post completo
]