# Generated by Django 4.1.2 on 2022-10-31 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_order_orderdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
