# Generated by Django 4.2.2 on 2023-07-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagement', '0006_alter_tasksmodel_execution_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='execution_status',
            field=models.BooleanField(choices=[(False, 'Pending'), (True, 'Completed')], default=False),
        ),
    ]