# Generated by Django 5.0 on 2025-07-04 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='telegram',
        ),
    ]
