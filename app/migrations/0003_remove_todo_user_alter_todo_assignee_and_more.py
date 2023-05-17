# Generated by Django 4.2 on 2023-05-12 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AlterField(
            model_name='todo',
            name='assignee',
            field=models.ForeignKey(limit_choices_to={'role': 'Employee'}, on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='assignor',
            field=models.ForeignKey(limit_choices_to={'role': 'Manager'}, on_delete=django.db.models.deletion.CASCADE, related_name='Managaer', to=settings.AUTH_USER_MODEL),
        ),
    ]
