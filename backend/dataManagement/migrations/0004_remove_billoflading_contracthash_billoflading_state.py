# Generated by Django 5.0.1 on 2024-03-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManagement', '0003_merge_20240324_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billoflading',
            name='contractHash',
        ),
        migrations.AddField(
            model_name='billoflading',
            name='state',
            field=models.CharField(default='in progress', max_length=100),
        ),
    ]
