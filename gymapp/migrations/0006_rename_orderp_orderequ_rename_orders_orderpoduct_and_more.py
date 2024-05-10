# Generated by Django 5.0.3 on 2024-05-03 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0005_ordere_orderp_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orderp',
            new_name='Orderequ',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Orderpoduct',
        ),
        migrations.RenameModel(
            old_name='Ordere',
            new_name='Ordersupli',
        ),
        migrations.AlterField(
            model_name='orderequ',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.equipment'),
        ),
        migrations.AlterField(
            model_name='orderpoduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.product'),
        ),
        migrations.AlterField(
            model_name='ordersupli',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.supliment'),
        ),
    ]
