# Generated by Django 4.2.5 on 2023-09-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_list_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='header',
            field=models.CharField(default='', max_length=20),
        ),
    ]
