# Generated by Django 4.2.20 on 2025-05-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0004_alter_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
