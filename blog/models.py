from django.db import models
from django.conf import settings
from django.utils import timezone

# Garantir que o 'POST' apagados do objeto is_deleted=True nunca sejam usados.
class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

#Modela a entidade Post
class Post(models.Model):


#Chave estrangeira para a entidade 'User' do Django
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='posts',
    verbose_name='Autor'

)

title = models.CharField('Título',max_length=127)
summary = models.CharField('Resumo',max_length=225)
created_at = models.DateTimeField('Criado em', default=timezone.now)
thumbnail = models.URLField('Miniatura (URL)')
textbody = models.TextField('Texto do post')
views = models.IntegerField('Visualizações', default=0)
is_active = models.BooleanField('Ativo', default=True)
is_deleted = models.BooleanField('Excluído', default=False)

objects = PostManager()         #Por padrão, só posts não apagados
all_objects = models.Manager()  #Permite acesso irrestrito, incluindo posts apagados

class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'


def __str__(self):
    return self.title