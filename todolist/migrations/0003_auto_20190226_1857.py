# Generated by Django 2.1.5 on 2019-02-26 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todo_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user_id',
            new_name='username',
        ),
    ]
