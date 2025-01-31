# Generated by Django 3.0.5 on 2020-04-10 07:34

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(6000000000)])),
                ('pin_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000)])),
                ('state', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('customer_user_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('customer_user_name', models.CharField(max_length=150)),
                ('product_size', models.CharField(max_length=3)),
                ('brand', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=10)),
                ('image_source', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=60)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
                ('image_source', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(6000000000)])),
                ('pin_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000)])),
                ('state', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('customer_user_name', models.CharField(max_length=150)),
                ('order_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=60)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('size_xs', models.BooleanField(default=False)),
                ('size_s', models.BooleanField(default=False)),
                ('size_m', models.BooleanField(default=False)),
                ('size_l', models.BooleanField(default=False)),
                ('size_xl', models.BooleanField(default=False)),
                ('size_xxl', models.BooleanField(default=False)),
                ('product_details', models.TextField()),
                ('image_main', models.ImageField(upload_to='images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kid', 'Kid')], default='Men', max_length=5)),
            ],
        ),
    ]
