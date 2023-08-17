# Generated by Django 4.2.4 on 2023-08-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_alter_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='link',
            field=models.URLField(verbose_name='Ссылка на страницу'),
        ),
    ]
