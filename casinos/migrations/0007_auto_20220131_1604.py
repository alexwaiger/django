# Generated by Django 3.1.1 on 2022-01-31 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0006_auto_20220131_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casino',
            name='trust_score',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='votes',
        ),
    ]
