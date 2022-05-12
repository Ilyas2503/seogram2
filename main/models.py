# coding=utf-8
from django.db import models


class Post(models.Model):
    '''
    author
    pud_date
    image
    description
    author_text
    category
    '''
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, verbose_name='Автор')
    pud_date = models.DateField(auto_now=True, verbose_name='Дата публикации')
    image_author = models.ImageField(upload_to='Post/author/%m/%d', blank=True, verbose_name='Фото автора')
    image_post = models.ImageField(upload_to='Post/post/%m/%d', blank=True, verbose_name='Фото поста')
    description = models.TextField()
    author_text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.author


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


