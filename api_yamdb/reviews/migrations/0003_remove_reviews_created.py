# Generated by Django 2.2.19 on 2022-06-26 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220623_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='created',
        ),
    ]