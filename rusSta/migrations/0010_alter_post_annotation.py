# Generated by Django 3.2.11 on 2022-01-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0009_auto_20220125_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='annotation',
            field=models.TextField(blank=True, default='', verbose_name='文章注释'),
        ),
    ]