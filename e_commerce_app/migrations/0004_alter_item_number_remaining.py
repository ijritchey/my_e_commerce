# Generated by Django 4.1.3 on 2022-12-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number_remaining',
            field=models.IntegerField(null=True),
        ),
    ]
