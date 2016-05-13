# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import internet_store


class User(models.Model):

    """ Класс для табилцы в БД с пользователями. """

    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.Email


class Product(models.Model):

    """ Класс для табилцы в БД с товарами. """

    ProductId = models.AutoField(primary_key=True)
    ProductTypeId = models.ForeignKey('internet_store.ProductType', on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=200)
    ProductPrice = models.DecimalField(max_digits=30, decimal_places=2)


class ProductType(models.Model):

    """ Класс для табилцы в БД с типами товаров. """

    ProductTypeId = models.AutoField(primary_key=True)
    ProductTypeName = models.CharField(max_length=200)


class Region(models.Model):

    """ Класс для табилцы в БД с районами доставки. """

    RegionId = models.AutoField(primary_key=True)
    RegionName = models.CharField(max_length=200)


class Street(models.Model):

    """ Класс для табилцы в БД с улицами. """

    StreetId = models.AutoField(primary_key=True)
    RegionId = models.ForeignKey(Region, on_delete=models.CASCADE)
    StreetName = models.CharField(max_length=200)


class Courier(models.Model):

    """ Класс для табилцы в БД с курьерами. """

    CourierId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    CourierName = models.CharField(max_length=200)


class MarketingSource(models.Model):

    """ Класс для табилцы в БД с источниками рекламы. """

    MarketingSourceId = models.AutoField(primary_key=True)
    MarketingSourceName = models.CharField(max_length=200)


class Delivery(models.Model):

    """ Класс для табилцы в БД с доставками. """

    DeliveryId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    DeliveryOrderDateTime = models.DateTimeField(auto_now_add=True)
    DeliveryCompleteDateTime = models.DateTimeField()
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductAmount = models.PositiveIntegerField()
    OrderTotalSum = models.DecimalField(max_digits=30, decimal_places=2)
    CourierId = models.ForeignKey(Courier, on_delete=models.CASCADE)
    MarketingSourceId = models.ForeignKey(MarketingSource, on_delete=models.CASCADE)
    StreetId = models.ForeignKey(Street, on_delete=models.CASCADE)
    House = models.PositiveIntegerField()
    Building = models.PositiveIntegerField()


