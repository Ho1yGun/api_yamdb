# Generated by Django 2.2.16 on 2022-06-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220630_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]