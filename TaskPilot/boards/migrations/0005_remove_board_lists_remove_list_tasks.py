# Generated by Django 5.0.4 on 2024-04-08 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_remove_list_board_id_list_board_name_task_list_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='lists',
        ),
        migrations.RemoveField(
            model_name='list',
            name='tasks',
        ),
    ]
