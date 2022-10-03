from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
         verbose_name_plural = 'Группы'
  

class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField('Дата публикации',auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Сообщество'
    )

    class Meta:
        ordering = (
            '-pub_date',
    )
        verbose_name = 'Записи'
