# Generated by Django 3.1.1 on 2022-01-11 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='currency',
        ),
    ]