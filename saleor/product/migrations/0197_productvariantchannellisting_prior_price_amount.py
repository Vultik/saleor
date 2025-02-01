# Generated by Django 4.2.16 on 2024-12-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0196_slug_unique_constraint"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariantchannellisting",
            name="prior_price_amount",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=12, null=True
            ),
        ),
    ]
