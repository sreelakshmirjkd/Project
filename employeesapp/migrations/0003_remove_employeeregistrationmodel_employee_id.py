# Generated by Django 5.1.4 on 2025-02-01 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0002_remove_employeeregistrationmodel_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeregistrationmodel',
            name='employee_id',
        ),
    ]
