# Generated by Django 4.2 on 2023-04-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
