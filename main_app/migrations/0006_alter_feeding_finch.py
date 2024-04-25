# Generated by Django 5.0.4 on 2024-04-25 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0005_alter_feeding_finch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feeding",
            name="finch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main_app.finch"
            ),
        ),
    ]
