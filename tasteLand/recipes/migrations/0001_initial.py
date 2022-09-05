# Generated by Django 4.0.6 on 2022-08-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Название категории')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографии')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название рецепта')),
                ('content', models.TextField(blank=True, verbose_name='Содержание рецепта')),
                ('dt_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dt_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографии')),
                ('is_publ', models.BooleanField(default=True, verbose_name='Публикация')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='recipes.category', verbose_name='Категория')),
            ],
        ),
    ]
