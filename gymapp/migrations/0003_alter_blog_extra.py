# Generated by Django 5.0.3 on 2024-04-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='extra',
            field=models.CharField(max_length=5000),
        ),
    ]
