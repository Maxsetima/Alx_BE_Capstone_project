# Generated by Django 5.1.7 on 2025-04-10 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_product_farmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('farmer', 'Farmer'), ('consumer', 'Consumer'), ('logistics', 'Logistics')], default='consumer', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
