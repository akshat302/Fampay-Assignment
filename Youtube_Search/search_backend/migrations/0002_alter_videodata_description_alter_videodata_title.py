 # Generated by Django 4.1.13 on 2024-01-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search_backend", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videodata",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="videodata",
            name="title",
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
