# Generated by Django 3.1.1 on 2022-01-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decor', '0007_auto_20220118_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='icons_color',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Черно-белые иконки'),
        ),
    ]