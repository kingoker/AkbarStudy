# Generated by Django 3.1.2 on 2020-10-18 01:56

import courses.utilities
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('content', models.TextField(verbose_name='О курсе')),
                ('image', models.ImageField(upload_to=courses.utilities.get_timestamp_path, verbose_name='Картинка')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('publish', models.BooleanField(default=True, verbose_name='Опубликовать?')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка на урок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('publish', models.BooleanField(default=True, verbose_name='Опубликовать?')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.rubric', verbose_name='Категория'),
        ),
    ]
