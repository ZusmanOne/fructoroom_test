# Generated by Django 4.2.4 on 2023-08-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.CharField(choices=[('music', 'music'), ('video', 'video'), ('website', 'website'), ('book', 'book'), ('article', 'article')], default='website', max_length=200, verbose_name='Тип ссылки'),
        ),
    ]