# Generated by Django 5.0.6 on 2024-05-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="cell_number",
            field=models.CharField(max_length=50),
        ),
    ]