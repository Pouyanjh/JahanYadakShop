# Generated by Django 4.2.4 on 2023-09-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_headlight_productid_lent_productid_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'orderitem', 'verbose_name_plural': 'orderitems'},
        ),
        migrations.AddField(
            model_name='order',
            name='orderproduct',
            field=models.TextField(default=2, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]