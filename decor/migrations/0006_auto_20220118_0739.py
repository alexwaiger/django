# Generated by Django 3.1.1 on 2022-01-18 07:39

import colorfield.fields
from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0005_auto_20220113_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='badge',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/site_badges/', verbose_name='Значек (справа от лого)'),
        ),
        migrations.AddField(
            model_name='theme',
            name='bg_mob_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (mobile 480px)'),
        ),
        migrations.AddField(
            model_name='theme',
            name='bg_tab_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (tablet 992px)'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='bg_color',
            field=colorfield.fields.ColorField(blank=True, default='#000000', image_field=None, max_length=7, null=True, samples=None, verbose_name='Цвет фона #RRGGBB'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='bg_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='upload/img/custom/', verbose_name='Фоновое изображение (desktop 1280px)'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', image_field=None, max_length=7, null=True, samples=None, verbose_name='Основной цвет #RRGGBB'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='h_color',
            field=colorfield.fields.ColorField(blank=True, default='#FFF000', image_field=None, max_length=7, null=True, samples=None, verbose_name='Цвет хедера #RRGGBB'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='upload/img/site_logos/', verbose_name='Логотип'),
        ),
    ]
