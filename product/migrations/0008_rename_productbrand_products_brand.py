# Generated by Django 4.2.4 on 2023-08-11 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_products_productbrand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='productbrand',
            new_name='brand',
        ),
    ]