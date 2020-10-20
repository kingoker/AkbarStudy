from django.db import models
from .utilities import get_timestamp_path


class Course(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    content = models.TextField(verbose_name='О курсе')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Картинка')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    price = models.IntegerField(default=0, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')
    category = models.ForeignKey('Rubric', verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка на урок')
    content = models.TextField(verbose_name='Описание', blank=True)
    publish = models.BooleanField(default=True, verbose_name='Опубликовать?')
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

