# Generated by Django 5.0.1 on 2024-03-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billoflading',
            name='contractAddress',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
