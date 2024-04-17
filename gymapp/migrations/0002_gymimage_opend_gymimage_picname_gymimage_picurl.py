# Generated by Django 5.0.3 on 2024-04-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymimage',
            name='opend',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gymimage',
            name='picname',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gymimage',
            name='picurl',
            field=models.FileField(default='-', upload_to=''),
        ),
    ]
