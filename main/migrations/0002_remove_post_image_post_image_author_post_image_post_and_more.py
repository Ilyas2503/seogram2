# Generated by Django 4.0 on 2022-05-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_author',
            field=models.ImageField(blank=True, upload_to='Post/author/%m/%d', verbose_name='Фото автора'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_post',
            field=models.ImageField(blank=True, upload_to='Post/post/%m/%d', verbose_name='Фото поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
