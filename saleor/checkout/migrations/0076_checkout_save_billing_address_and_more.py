# Generated by Django 4.2.15 on 2025-02-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0075_merge_20250210_1203"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="save_billing_address",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="checkout",
            name="save_shipping_address",
            field=models.BooleanField(default=True),
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE checkout_checkout
            ALTER COLUMN save_billing_address
            SET DEFAULT true;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="""
            ALTER TABLE checkout_checkout
            ALTER COLUMN save_shipping_address
            SET DEFAULT true;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
