# Generated by Django 5.1.1 on 2024-11-28 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orders_user_remove_orderdetails_cart_item_and_more'),
        ('payment', '0002_alter_payment_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]