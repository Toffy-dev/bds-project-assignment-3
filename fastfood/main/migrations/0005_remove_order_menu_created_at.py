# Generated by Django 4.0 on 2021-12-31 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_customer_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_menu',
            name='created_at',
        ),
    ]
