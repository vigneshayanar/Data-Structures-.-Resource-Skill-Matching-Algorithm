# Generated by Django 3.2.25 on 2024-08-21 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_task_assigned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='projects',
        ),
    ]
