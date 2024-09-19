# Generated by Django 5.1.1 on 2024-09-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_buyer_age_game_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(db_default=True)),
                ('year_of_manufactory', models.IntegerField(default=None)),
            ],
        ),
    ]
