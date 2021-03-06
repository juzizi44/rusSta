# Generated by Django 3.2.11 on 2022-01-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0018_auto_20220127_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'verbose_name': 'hi', 'verbose_name_plural': 'hi'},
        ),
        migrations.RenameField(
            model_name='dog',
            old_name='name',
            new_name='ss',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='people',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='title',
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(2, '展示'), (1, '隐藏')], default=2, verbose_name='状态'),
        ),
    ]
