# Generated by Django 5.1.7 on 2025-04-10 04:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_order_consumer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
