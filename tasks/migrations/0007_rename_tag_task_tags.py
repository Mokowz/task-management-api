# Generated by Django 5.0.1 on 2024-01-16 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_rename_tags_task_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tag',
            new_name='tags',
        ),
    ]
