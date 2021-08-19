# Generated by Django 3.2.6 on 2021-08-19 16:31

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210819_1731'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='book',
            name='NewGinIndex',
        ),
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title'], name='NewGinIndex'),
        ),
    ]
