# Generated by Django 4.2.4 on 2023-08-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_car_delete_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopSells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topsellproductitle', models.CharField(blank=True, max_length=200)),
                ('price', models.CharField(blank=True, max_length=200)),
                ('image', models.URLField(blank=True)),
                ('exiting', models.BooleanField(default=True)),
                ('car', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
