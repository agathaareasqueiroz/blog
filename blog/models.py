# blog/models.py
 
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
 
 
class UserManager(BaseUserManager):
    # Garante que 'User' apagado `is_deleted=True` nunca seja usado
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
 
 
class User(AbstractUser):
    # Usuário personalizado
 
    # Remove os campos de 'name' originais
    first_name = None
    last_name = None
 
    # Substituímos pelo campo 'name'
    name = models.CharField('Nome', max_length=100)
 
    # Data de nascimento
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)
 
    # Thumbnail
    image = models.ImageField('Foto de perfil', upload_to='profiles/', null=True, blank=True)
 
    # Dados adicionais
    metadata = models.TextField('Informações', null=True, blank=True)
 
    # Soft delete
    is_deleted = models.BooleanField('Excluído', default=False)
 
    objects = UserManager()             # Por padrão, só 'User' não apagado
    all_objects = models.Manager()      # Permite acesso irrestrito, incluindo 'User' apagado
 
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
 
    def __str__(self):
        return self.name
 
 
class PostManager(models.Manager):
    # Garante que posts apagados, agendados ou de usuários
    # apagados nunca sejam utilizados nas consultas padrão.
    def get_queryset(self):
        return super().get_queryset().filter(
            is_deleted=False,
            user__is_deleted=False,
            created_at__lte=timezone.now()
        )
 
 
class Post(models.Model):
 
    # Chave estrangeira para a entidade 'User' do Django
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Autor'
    )
 
    # Modela a entidade 'Post'
    title = models.CharField('Título', max_length=127)
    summary = models.CharField('Resumo', max_length=255)
    created_at = models.DateTimeField('Criado em', default=timezone.now)
    thumbnail = models.URLField('Miniatura (URL)')
    textbody = models.TextField('Texto do post')
    views = models.IntegerField('Visualizações', default=0)
    is_active = models.BooleanField('Ativo', default=True)
    is_deleted = models.BooleanField('Excluído', default=False)
 
    objects = PostManager()         # Por padrão, só posts não apagados
    all_objects = models.Manager()  # Permite acesso irrestrito, incluindo posts apagados
 
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
 
    def __str__(self):
        return self.title