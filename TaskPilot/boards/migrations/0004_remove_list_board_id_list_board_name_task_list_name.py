# Generated by Django 5.0.4 on 2024-04-08 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_alter_board_name_alter_list_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='board_id',
        ),
        migrations.AddField(
            model_name='list',
            name='board_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.board'),
        ),
        migrations.AddField(
            model_name='task',
            name='list_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.list'),
        ),
    ]
