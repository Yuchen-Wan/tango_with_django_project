# Generated by Django 2.1.5 on 2021-07-29 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20210728_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
    ]
