# Generated by Django 3.1.1 on 2022-01-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Postback',
                'verbose_name_plural': 'Postbacks',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('postbacks', models.ManyToManyField(blank=True, related_name='partner_program', to='postbacks.Postback')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
    ]