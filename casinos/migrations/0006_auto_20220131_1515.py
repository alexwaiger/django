# Generated by Django 3.1.1 on 2022-01-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0005_auto_20220131_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='real_position',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Real Position'),
        ),
    ]
