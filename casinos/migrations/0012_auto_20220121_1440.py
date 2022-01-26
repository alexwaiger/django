# Generated by Django 3.1.1 on 2022-01-21 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postbacks', '0002_auto_20220121_1416'),
        ('casinos', '0011_auto_20220121_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aff', to='postbacks.partner'),
        ),
    ]
