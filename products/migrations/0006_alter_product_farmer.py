# Generated by Django 5.1.7 on 2025-04-09 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_customuser_password_alter_customuser_username_and_more'),
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser'),
        ),
    ]
