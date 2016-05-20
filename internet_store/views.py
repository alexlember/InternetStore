import json

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from internet_store import controller


# Create your views here.


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user_name = body['userName']
        email = body['email']

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        result = controller.safe_add_new_user(email, user_name)
        if result['Success'] is False:
            if 'Duplicate user email' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        users = controller.get_all_users()
        users_json = json.dumps(users)
        return HttpResponse(users_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        controller.delete_user(email)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def courier(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        courier_name = body['courierName']
        email = body['email']

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        result = controller.safe_add_new_courier(courier_name, email)
        if result['Success'] is False:
            if 'Duplicate courier name' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        couriers = controller.get_all_couriers()
        couriers_json = json.dumps(couriers)
        return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        courier_name = body['courierName']
        controller.delete_courier(courier_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def product_type(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product_type_name = body['productType']
        result = controller.safe_add_new_product_type(product_type_name)
        if result['Success'] is False:
            if 'Duplicate product_type' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        product_types = controller.get_all_product_types()
        product_types_json = json.dumps(product_types)
        return HttpResponse(product_types_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product_type_name = body['productType']
        controller.delete_product_type(product_type_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def product(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product_name = body['product']
        pr_type = body['productType']
        price = body['price']
        result = controller.safe_add_new_product(product_name, pr_type, price)
        if result['Success'] is False:
            if 'Duplicate product:' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        products = controller.get_all_products()
        products_json = json.dumps(products)
        return HttpResponse(products_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product_name = body['product']
        controller.delete_product(product_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def marketing_source(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        marketing_source_name = body['marketingSource']
        result = controller.safe_add_new_marketing_source(marketing_source_name)
        if result['Success'] is False:
            if 'Duplicate marketing source' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        marketing_sources = controller.get_all_marketing_sources()
        marketing_sources_json = json.dumps(marketing_sources)
        return HttpResponse(marketing_sources_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        marketing_source_name = body['marketingSource']
        controller.delete_marketing_source(marketing_source_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def region(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        region_name = body['region']
        result = controller.safe_add_new_region(region_name)
        if result['Success'] is False:
            if 'Duplicate region' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        regions = controller.get_all_regions()
        regions_json = json.dumps(regions)
        return HttpResponse(regions_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        region_name = body['region']
        controller.delete_region(region_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def street(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)
        street_name = body['street']
        region_name = body['region']
        result = controller.safe_add_new_street(street_name, region_name)
        if result['Success'] is False:
            if 'Duplicate street:' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        streets = controller.get_all_streets()
        streets_json = json.dumps(streets)
        return HttpResponse(streets_json, content_type="application/json")
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        street_name = body['street']
        controller.delete_street(street_name)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def generate(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)
        user_email = body['user']
        controller.generate_delivery(user_email)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def reload_deliveries(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)
        user_email = body['user']
        controller.reload_all_deliveries(user_email)
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def delivery(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)

        delivery_obj = DeliveryDTO.make_delivery(body['user'],
                                                 body['courier'],
                                                 body['productType'],
                                                 body['product'],
                                                 body['quantity'],
                                                 body['street'],
                                                 body['region'],
                                                 body['marketingSource'],
                                                 body['home'],
                                                 body['building'],
                                                 body['deliveryDate'],
                                                 body['deliveryTime'])

        result = controller.save_delivery(delivery_obj)
        if result['Success'] is False:
            if 'Duplicate street:' in result['Message']:
                return HttpResponseBadRequest(result['Message'])

    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


class DeliveryDTO(object):
    user_name = ""
    courier_name = ""
    product_type_label = ""
    product_label = ""
    quantity = 0
    street_label = ""
    region_label = ""
    marketing_source_label = ""
    home = 1
    building = 1
    delivery_date = ""
    delivery_time = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self,
                 user_name,
                 courier_name,
                 product_type_label,
                 product_label,
                 quantity,
                 street_label,
                 region_label,
                 marketing_source_label,
                 home,
                 building,
                 delivery_date,
                 delivery_time):
        self.user_name = user_name
        self.courier_name = courier_name
        self.product_type_label = product_type_label
        self.product_label = product_label
        self.quantity = quantity
        self.street_label = street_label
        self.region_label = region_label
        self.marketing_source_label = marketing_source_label
        self.home = home
        self.building = building
        self.delivery_date = delivery_date
        self.delivery_time = delivery_time

    @staticmethod
    def make_delivery(user_name,
                      courier_name,
                      product_type_label,
                      product_label,
                      quantity,
                      street_label,
                      region_label,
                      marketing_source_label,
                      home,
                      building,
                      delivery_date,
                      delivery_time):
        delivery_obj = DeliveryDTO(user_name, courier_name, product_type_label,
                                   product_label, quantity, street_label, region_label,
                                   marketing_source_label, home, building, delivery_date, delivery_time)
        return delivery_obj
