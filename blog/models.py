# blog\models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class PostManager(models.Manager):
    # Manager de 'post'
    # Define algumas das Regras de Negócio
    def get_queryset(self):
        return super().get_queryset().filter(
            is_deleted=False#,                   # Não mostra post se apagado
            #user__is_deleted=False,             # Não mostra post se usuário apagado
            #created_at__lte=timezone.now()      # Não mostra post se do futuro
        )

# Modela a entidade 'Post'
class Post(models.Model):
  
    # Chave estrangeira para a entidade 'User' do Django
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Autor'
    )

    title = models.CharField('Título', max_length=127)
    summary = models.CharField('Resumo', max_length=255)
    created_at = models.DateTimeField('Criado em', default=timezone.now)
    thumbnail = models.URLField('URL da Imagem')
    textbody = models.TextField('Texto do post')
    views = models.IntegerField('Visualizações', default=0)
    is_comment = models.BooleanField('Permitir comentários', default=True)
    is_active = models.BooleanField('Ativo', default=True)
    is_deleted = models.BooleanField('Excluído', default=False)
 
    objects = PostManager()         # Por padrão, só posts não apagados
    all_objects = models.Manager()  # Permite acesso irrestrito, incluindo posts apagados

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title