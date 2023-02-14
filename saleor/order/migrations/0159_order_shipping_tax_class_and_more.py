# Generated by Django 4.0.7 on 2022-10-20 11:55

from django.db import migrations, models
import django.db.models.deletion
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):
    dependencies = [
        ("tax", "0005_migrate_vatlayer"),
        ("order", "0158_migrate_base_shipping_price_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipping_tax_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tax.taxclass",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_tax_class_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_tax_class_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_tax_class_private_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="tax_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="tax.taxclass",
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="tax_class_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="tax_class_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="orderline",
            name="tax_class_private_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="shipping_tax_rate",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="tax_rate",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=5, null=True
            ),
        ),
    ]
