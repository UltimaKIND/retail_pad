# Generated by Django 5.1.3 on 2024-11-29 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retail_pad", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="node",
            name="supplier",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="retail_pad.node",
                verbose_name="поставщик",
            ),
        ),
    ]
