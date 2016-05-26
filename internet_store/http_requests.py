# coding=utf-8
import urllib
import urllib2

from internet_store.models import User, Region, Street, Courier, ProductType, Product, MarketingSource


def send_delivery(delivery):

    user = User.objects.get(UserId=delivery.UserId_id)
    order_date_time = delivery.DeliveryOrderDateTime
    complete_date_time = delivery.DeliveryCompleteDateTime
    city = 'Москва'
    region = Region.objects.get(RegionId=delivery.RegionId_id)
    street = Street.objects.get(StreetId=delivery.StreetId_id)
    home = delivery.House
    building = delivery.Building
    courier = Courier.objects.get(CourierId=delivery.CourierId_id)
    product_type = ProductType.objects.get(ProductTypeId=delivery.ProductTypeId_id)
    product = Product.objects.get(ProductId=delivery.ProductId_id)
    marketing_source = MarketingSource.objects.get(MarketingSourceId=delivery.MarketingSourceId_id)
    total_sum = delivery.OrderTotalSum

    post_data = [('user', user.Email),
                 ('order_date_time', order_date_time),
                 ('complete_date_time', complete_date_time),
                 ('city', city),
                 ('region', region.RegionName.encode("utf-8")),
                 ('street', street.StreetName.encode("utf-8")),
                 ('home', home),
                 ('building', building),
                 ('courier', courier.CourierName.encode("utf-8")),
                 ('product_type', product_type.ProductTypeName.encode("utf-8")),
                 ('product', product.ProductName.encode("utf-8")),
                 ('marketing_source', marketing_source.MarketingSourceName.encode("utf-8")),
                 ('total_sum', total_sum)]

    try:
        result = urllib2.urlopen('http://localhost:8500/dhm/delivery/', urllib.urlencode(post_data))
        content = result.read()
        if 'Success' in content:
            result = {'Success': True}
    except urllib2.HTTPError as err:
        result = {'Success': False, 'Message': err.msg + ' on the remote server Delivery Heat Map', 'Code': err.code}

    return result


def reload_deliveries(user_email):
    pass    #r = requests.post(url='http://localhost:90000/delivery', data={'хуй':'пизда'}, )