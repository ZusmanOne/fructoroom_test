from django.db import models
from django.conf import settings

PAGE_TYPES = (
    ('music', 'music'),
    ('video', 'video'),
    ('website', 'website'),
    ('book', 'book'),
    ('article', 'article')
)


class Page(models.Model):
    title = models.CharField('Заголовок страницы', max_length=200)
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='pages',
        verbose_name='Пользователь'
    )
    collection = models.ManyToManyField(
        'Collection',
        blank=True,
        related_name='pages',
        verbose_name='Коллекция'
    )
    type = models.CharField('Тип ссылки', choices=PAGE_TYPES, default='website')
    description = models.TextField('Краткое описание')
    link = models.URLField('Ссылка на страницу', blank=True)
    image = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "Закладка"
        verbose_name_plural = "Закладки"

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField('Название коллекции', max_length=200)
    description = models.TextField('Краткое описание')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.title
