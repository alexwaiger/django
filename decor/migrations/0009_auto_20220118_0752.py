# Generated by Django 3.1.1 on 2022-01-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0008_theme_icons_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='icons_color',
            field=models.BooleanField(blank=True, default=False, verbose_name='Черно-белые иконки'),
        ),
    ]