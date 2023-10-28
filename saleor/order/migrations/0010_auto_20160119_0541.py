# Generated by Django 1.9.1 on 2016-01-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("order", "0009_auto_20151201_0820")]

    operations = [
        migrations.RemoveField(model_name="deliverygroup", name="shipping_method"),
        migrations.RemoveField(model_name="deliverygroup", name="shipping_required"),
        migrations.RemoveField(model_name="order", name="shipping_method"),
        migrations.AddField(
            model_name="deliverygroup",
            name="shipping_method_name",
            field=models.CharField(
                blank=True, default=None, editable=False, max_length=255, null=True
            ),
        ),
    ]
