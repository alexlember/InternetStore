# coding=utf-8
from __future__ import print_function

import random
import datetime  # import datetime, timedelta
from datetime import timedelta

import dateutil.parser
import pytz
from django.db.utils import IntegrityError
from pytz import timezone

from internet_store.models import User, Courier, ProductType, Product, MarketingSource, Region, Street, Delivery


def get_all_users():
    users = User.objects.all()
    modified_users = []
    for u in users:
        modified_user = {'Email': u.Email, 'UserName': u.UserName}
        modified_users.append(modified_user)
    return modified_users


def safe_add_new_user(email, user_name):
    user = User(Email=email, UserName=user_name)
    try:
        user.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate user email address: ' + email}
    return result


def delete_user(email):
    user = User.objects.get(Email=email)
    user.delete()
    result = {'Success': True}
    return result


def get_all_couriers():
    couriers = Courier.objects.all()
    modified_couriers = []
    for c in couriers:
        courier_user = User.objects.get(UserId=c.UserId_id)
        modified_courier = {'CourierName': c.CourierName, 'CourierUser': courier_user.Email}
        modified_couriers.append(modified_courier)
    return modified_couriers


def safe_add_new_courier(courier_name, email):
    user_id = User.objects.get(Email=email)
    courier = Courier(CourierName=courier_name, UserId=user_id)
    try:
        courier.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    return result


def delete_courier(courier_name):
    courier = Courier.objects.get(CourierName=courier_name)
    courier.delete()
    result = {'Success': True}
    return result


def get_all_product_types():
    product_types = ProductType.objects.all()
    modified_product_types = []
    for pt in product_types:
        modified_product_type = {'ProductTypeName': pt.ProductTypeName}
        modified_product_types.append(modified_product_type)
    return modified_product_types


def safe_add_new_product_type(product_type_name):
    product_type = ProductType(ProductTypeName=product_type_name)
    try:
        product_type.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate product_type: ' + product_type_name}
    return result


def delete_product_type(product_type):
    product_type = ProductType.objects.get(ProductTypeName=product_type)
    product_type.delete()
    result = {'Success': True}
    return result


def get_all_products():
    products = Product.objects.all()
    modified_products = []
    for p in products:
        pr_type = ProductType.objects.get(ProductTypeId=p.ProductTypeId_id)
        modified_product = {'ProductLabel': p.ProductName,
                            'Price': str(p.ProductPrice),
                            'ProductType': pr_type.ProductTypeName}
        modified_products.append(modified_product)
    return modified_products


def safe_add_new_product(product_name, product_type, price):
    product_type_id = ProductType.objects.get(ProductTypeName=product_type)
    product = Product(ProductName=product_name, ProductTypeId=product_type_id, ProductPrice=price)
    try:
        product.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate product: ' + product_name}
    return result


def delete_product(product_name):
    product = Product.objects.get(ProductName=product_name)
    product.delete()
    result = {'Success': True}
    return result


def get_all_marketing_sources():
    marketing_sources = MarketingSource.objects.all()
    modified_marketing_sources = []
    for ms in marketing_sources:
        modified_marketing_source = {'MarketingSourceLabel': ms.MarketingSourceName}
        modified_marketing_sources.append(modified_marketing_source)
    return modified_marketing_sources


def safe_add_new_marketing_source(ms):
    marketing_source = MarketingSource(MarketingSourceName=ms)
    try:
        marketing_source.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate marketing source: ' + ms}
    return result


def delete_marketing_source(marketing_source_name):
    marketing_source = MarketingSource.objects.get(MarketingSourceName=marketing_source_name)
    marketing_source.delete()
    result = {'Success': True}
    return result


def get_all_regions():
    regions = Region.objects.all()
    modified_regions = []
    for r in regions:
        modified_region = {'RegionName': r.RegionName}
        modified_regions.append(modified_region)
    return modified_regions


def safe_add_new_region(region_name):
    region = Region(RegionName=region_name)
    try:
        region.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate region: ' + region_name}
    return result


def delete_region(region_name):
    region = Region.objects.get(RegionName=region_name)
    region.delete()
    result = {'Success': True}
    return result


def get_all_streets():
    streets = Street.objects.all()
    modified_streets = []
    for s in streets:
        region = Region.objects.get(RegionId=s.RegionId_id)
        modified_street = {'StreetName': s.StreetName,
                           'Region': region.RegionName}
        modified_streets.append(modified_street)
    return modified_streets


def safe_add_new_street(street_name, region_name):
    region = Region.objects.get(RegionName=region_name)
    street = Street(StreetName=street_name, RegionId=region)
    try:
        street.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate street: ' + street_name}
    return result


def delete_street(street_name):
    street = Street.objects.get(StreetName=street_name)
    street.delete()
    result = {'Success': True}
    return result


def save_delivery(delivery_obj):
    user_id = User.objects.get(Email=delivery_obj.user_name)
    courier_id = Courier.objects.get(CourierName=delivery_obj.courier_name)
    product_type_id = ProductType.objects.get(ProductTypeName=delivery_obj.product_type_label)
    product_id = Product.objects.get(ProductName=delivery_obj.product_label)
    region_id = Region.objects.get(RegionName=delivery_obj.region_label)
    street_id = Street.objects.get(StreetName=delivery_obj.street_label)
    marketing_source_id = MarketingSource.objects.get(MarketingSourceName=delivery_obj.marketing_source_label)
    home = delivery_obj.home
    building = delivery_obj.building
    quantity = delivery_obj.quantity

    total_sum = float(product_id.ProductPrice) * quantity

    delivery_date = dateutil.parser.parse(delivery_obj.delivery_date).astimezone(timezone('US/Pacific'))
    delivery_time = dateutil.parser.parse(delivery_obj.delivery_time).astimezone(timezone('US/Pacific'))

    delivery_order_date_time = datetime.datetime(delivery_date.year, delivery_date.month, delivery_date.day,
                                                 delivery_time.hour, delivery_time.minute, delivery_time.second)

    possible_delivery_time = [timedelta(minutes=23),
                              timedelta(minutes=35),
                              timedelta(minutes=39),
                              timedelta(minutes=40),
                              timedelta(minutes=48),
                              timedelta(minutes=56),
                              timedelta(hours=1, minutes=13),
                              timedelta(hours=2, minutes=4),
                              timedelta(hours=1, minutes=34)]

    random_timedelta = random.choice(possible_delivery_time)

    delivery_complete_date_time = delivery_order_date_time + random_timedelta

    delivery = Delivery(UserId=user_id, CourierId=courier_id, ProductTypeId=product_type_id,
                        ProductId=product_id, RegionId=region_id, StreetId=street_id,
                        MarketingSourceId=marketing_source_id, House=home, Building=building,
                        ProductAmount=quantity, OrderTotalSum=total_sum,
                        DeliveryOrderDateTime=delivery_order_date_time,
                        DeliveryCompleteDateTime=delivery_complete_date_time)

    delivery.save()
    result = {'Success': True}

    return result


def generate_delivery(user_email):
    user_id = User.objects.get(Email=user_email)

    couriers = Courier.objects.filter(UserId=user_id)
    random_courier = random.choice(couriers)

    if user_id.Email == 'alexlember@test.ru':
        prod_type = ProductType.objects.get(ProductTypeName='пицца')
    elif user_id.Email == 'smadamin@test.ru':
        prod_type = ProductType.objects.get(ProductTypeName='телефоны')
    else:
        prod_type = ProductType.objects.get(ProductTypeName='пицца')

    products = Product.objects.filter(ProductTypeId=prod_type)
    random_product = random.choice(products)

    if user_id.Email == 'alexlember@test.ru':
        region = Region.objects.get(RegionName='Новокосино')
    elif user_id.Email == 'smadamin@test.ru':
        region = Region.objects.get(RegionName='Косино-Ухтомский')
    else:
        region = Region.objects.get(RegionName='Выхино')

    streets = Street.objects.filter(RegionId=region)
    random_street = random.choice(streets)

    marketing_sources = MarketingSource.objects.all()
    random_marketing_source = random.choice(marketing_sources)

    homes = range(1, 30)
    random_home = random.choice(homes)

    buildings = range(1, 10)
    random_building = random.choice(buildings)

    quantities = range(1, 3)
    random_quantity = random.choice(quantities)

    total_sum = float(random_product.ProductPrice) * random_quantity

    current_date_time = datetime.datetime.now().replace(tzinfo=pytz.timezone('US/Pacific'))

    possible_order_times = [timedelta(days=1, minutes=30),
                            timedelta(days=1, hours=4),
                            timedelta(days=2, hours=7),
                            timedelta(days=2, hours=11),
                            timedelta(days=3, hours=2),
                            timedelta(days=3, hours=3, minutes=13)]
    random_order_timedelta = random.choice(possible_order_times)
    delivery_order_date_time = current_date_time + random_order_timedelta

    possible_delivery_complete_times = [timedelta(minutes=23),
                                        timedelta(minutes=35),
                                        timedelta(minutes=39),
                                        timedelta(minutes=40),
                                        timedelta(minutes=48),
                                        timedelta(minutes=56),
                                        timedelta(hours=1, minutes=13),
                                        timedelta(hours=2, minutes=4),
                                        timedelta(hours=1, minutes=34)]

    random_complete_timedelta = random.choice(possible_delivery_complete_times)

    delivery_complete_date_time = delivery_order_date_time + random_complete_timedelta

    delivery = Delivery(UserId=user_id, CourierId=random_courier, ProductTypeId=prod_type,
                        ProductId=random_product, RegionId=region, StreetId=random_street,
                        MarketingSourceId=random_marketing_source, House=random_home, Building=random_building,
                        ProductAmount=random_quantity, OrderTotalSum=total_sum,
                        DeliveryOrderDateTime=delivery_order_date_time,
                        DeliveryCompleteDateTime=delivery_complete_date_time)

    delivery.save()
    result = {'Success': True}

    return result


def reload_all_deliveries(user_email):
    user_id = User.objects.get(Email=user_email)
    # delete all deliveries on DHM service
    # upload all deliveries again there
    pass
