# Generated by Django 2.2.16 on 2022-03-05 13:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220301_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.AddField(
            model_name='titles',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(related_name='titles', to='reviews.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='titles',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Выберите категорию', max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[-a-zA-Z0-9_]+$', 'Please only use alphabetic characters, numbers and underscores')], verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.DeleteModel(
            name='Genre_title',
        ),
    ]
