# Generated by Django 2.2.19 on 2022-06-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220627_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
