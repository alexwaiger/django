# Generated by Django 3.1.1 on 2022-01-12 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0006_countries_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
    ]
