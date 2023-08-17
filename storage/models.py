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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pages',
        verbose_name='Пользователь'
    )
    collection = models.ManyToManyField(
        'Collection',
        blank=True,
        related_name='pages',
        verbose_name='Коллекция'
    )
    type = models.CharField('Тип ссылки', choices=PAGE_TYPES, max_length=200, default='website')
    description = models.TextField('Краткое описание')
    link = models.URLField('Ссылка на страницу')
    image = models.URLField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "Закладка"
        verbose_name_plural = "Закладки"

    def __str__(self):
        return f'Закладка - {self.title}'


class Collection(models.Model):
    title = models.CharField('Название коллекции', max_length=200)
    description = models.TextField('Краткое описание', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return f'Коллекция - {self.title}'
