# Generated by Django 5.0.6 on 2024-05-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LogEntry",
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
                ("measurement_time", models.DateTimeField(auto_now_add=True)),
                ("upper_power2", models.FloatField()),
                ("upper_snr", models.FloatField()),
                ("lower_power", models.FloatField()),
                ("lower_snr", models.FloatField()),
                ("cell_number", models.CharField(max_length=100)),
            ],
        ),
    ]
