# Generated by Django 5.1.1 on 2024-09-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_phones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phones',
            old_name='year_of_manufactory',
            new_name='year_of_release',
        ),
    ]
