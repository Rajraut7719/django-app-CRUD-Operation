# Generated by Django 3.0.5 on 2022-04-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220405_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='time',
            field=models.DateTimeField(default=''),
        ),
    ]
