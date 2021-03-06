# Generated by Django 3.2.11 on 2022-01-27 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0011_auto_20220127_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rusSta.userinfo', verbose_name='收藏人')),
                ('title', models.ForeignKey(max_length=61, on_delete=django.db.models.deletion.CASCADE, to='rusSta.post', verbose_name='收藏文章')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]
