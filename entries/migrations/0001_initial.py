# Generated by Django 5.2 on 2025-04-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "entries",
            },
        ),
    ]
