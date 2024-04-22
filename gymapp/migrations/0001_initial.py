# Generated by Django 5.0.3 on 2024-04-21 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('edetails', models.TextField()),
                ('ecount', models.IntegerField(default=0)),
                ('eimage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='GymImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gymname', models.CharField(max_length=100)),
                ('gymemail', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('mgymtime', models.CharField(max_length=100)),
                ('egymtime', models.CharField(max_length=100)),
                ('maplink', models.CharField(max_length=1000)),
                ('addressline1', models.CharField(max_length=255)),
                ('addressline2', models.CharField(max_length=255)),
                ('addressline3', models.CharField(max_length=255)),
                ('addressline4', models.CharField(max_length=255)),
                ('addressline5', models.CharField(max_length=255)),
                ('addressline6', models.CharField(max_length=255)),
                ('instalink', models.URLField(blank=True)),
                ('fblink', models.URLField(blank=True)),
                ('ytlink', models.URLField(blank=True)),
                ('ownername', models.CharField(max_length=100)),
                ('picname', models.FileField(upload_to='')),
                ('picurl', models.FileField(default='-', upload_to='')),
                ('experience', models.CharField(max_length=50)),
                ('opend', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GymImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gymmedia/')),
            ],
        ),
        migrations.CreateModel(
            name='NewMemberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Onsite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='registerm',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=100)),
                ('picname', models.FileField(upload_to='')),
                ('picurl', models.FileField(default='-', upload_to='')),
                ('dob', models.DateField(null=True)),
                ('start', models.DateField(null=True)),
                ('weight', models.CharField(max_length=10)),
                ('heightf', models.CharField(max_length=10)),
                ('heighti', models.CharField(max_length=10)),
                ('membershipplan', models.CharField(choices=[('1month', '1month'), ('3months', '3months'), ('6months', '6months'), ('9months', '9months'), ('12months', '12months')], max_length=100)),
                ('trainer', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('feeamount', models.CharField(max_length=10)),
                ('pay', models.CharField(choices=[('Cash', 'Cash'), ('Online', 'Online')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='supliment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sdetails', models.TextField()),
                ('scount', models.IntegerField(default=0)),
                ('simage', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=100)),
                ('mobile', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=100)),
                ('picname', models.FileField(upload_to='')),
                ('picurl', models.FileField(default='-', upload_to='')),
                ('dob', models.DateField(null=True)),
                ('start', models.DateField(null=True)),
                ('weight', models.CharField(max_length=10)),
                ('heightf', models.CharField(max_length=10)),
                ('heighti', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('amount', models.TextField()),
                ('membernumber', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='equipmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eimage', models.ImageField(upload_to='product_images')),
                ('eproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gymapp.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gymapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='suplimentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simage', models.ImageField(upload_to='product_images')),
                ('sproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gymapp.supliment')),
            ],
        ),
    ]
