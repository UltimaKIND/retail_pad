# Generated by Django 5.1.3 on 2024-12-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retail_pad", "0003_alter_node_supplier"),
    ]

    operations = [
        migrations.AddField(
            model_name="node",
            name="network_lvl",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
