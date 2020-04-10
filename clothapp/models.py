from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
# Create your models here.
CATEGORY = (("Men", "Men"), ("Women", "Women"), ("Kid", "Kid"))


class Product(models.Model):
    brand = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=60, null=False)
    price = models.IntegerField(validators=[MinValueValidator(1)], null=False)
    size_xs = models.BooleanField(default=False)
    size_s = models.BooleanField(default=False)
    size_m = models.BooleanField(default=False)
    size_l = models.BooleanField(default=False)
    size_xl = models.BooleanField(default=False)
    size_xxl = models.BooleanField(default=False)
    product_details = models.TextField(null=False)
    image_main = models.ImageField(
        upload_to="images/", blank=False, null=False)
    image_2 = models.ImageField(upload_to="images/", blank=True, null=True)
    image_3 = models.ImageField(upload_to="images/", blank=True, null=True)
    image_4 = models.ImageField(upload_to="images/", blank=True, null=True)
    image_5 = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.CharField(max_length=5, choices=CATEGORY, default="Men")

    def __str__(self):
        return self.brand + " " + self.description


class Cart(models.Model):
    product_id = models.IntegerField(
        validators=[MinValueValidator(1)], null=False)
    customer_user_name = models.CharField(max_length=150)
    product_size = models.CharField(max_length=3)
    brand = models.CharField(max_length=25)
    description = models.CharField(max_length=60)
    price = models.IntegerField()
    category = models.CharField(max_length=10)
    image_source = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.product_id)+' '+self.product_size + ' '+self.customer_user_name


class Address(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(validators=[MinValueValidator(6000000000)])
    pin_code = models.IntegerField(validators=[MinValueValidator(100000)])
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    customer_user_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name + ' ' + self.city + ' ' + self.locality


class Order(models.Model):
    brand = models.CharField(max_length=25)
    description = models.CharField(max_length=60)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateTimeField(default=datetime.now)
    image_source = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(validators=[MinValueValidator(6000000000)])
    pin_code = models.IntegerField(validators=[MinValueValidator(100000)])
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    customer_user_name = models.CharField(max_length=150)
    order_id = models.IntegerField()

    def __str__(self):
        return self.customer_user_name + ' ' + str(self.order_id)
