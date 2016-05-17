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
        email = body['userEmail']
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
        user_email = body['userEmail']

        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        result = controller.safe_add_new_courier(courier_name, user_email)
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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass
        # # create a form instance and populate it with data from the request:
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # user_email = body['userEmail']
        #
        # # process the data in form.cleaned_data as required
        # # ...
        # # redirect to a new URL:
        # result = controller.safe_add_new_courier(courier_name, user_email)
        # if result['Success'] is False:
        #     if 'Duplicate courier name' in result['Message']:
        #         return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        pass
        # couriers = controller.get_all_couriers()
        # couriers_json = json.dumps(couriers)
        # return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # controller.delete_courier(courier_name)
    else:
        pass
        # return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass
        # # create a form instance and populate it with data from the request:
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # user_email = body['userEmail']
        #
        # # process the data in form.cleaned_data as required
        # # ...
        # # redirect to a new URL:
        # result = controller.safe_add_new_courier(courier_name, user_email)
        # if result['Success'] is False:
        #     if 'Duplicate courier name' in result['Message']:
        #         return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        pass
        # couriers = controller.get_all_couriers()
        # couriers_json = json.dumps(couriers)
        # return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # controller.delete_courier(courier_name)
    else:
        pass
        # return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def marketing_source(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass
        # # create a form instance and populate it with data from the request:
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # user_email = body['userEmail']
        #
        # # process the data in form.cleaned_data as required
        # # ...
        # # redirect to a new URL:
        # result = controller.safe_add_new_courier(courier_name, user_email)
        # if result['Success'] is False:
        #     if 'Duplicate courier name' in result['Message']:
        #         return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        pass
        # couriers = controller.get_all_couriers()
        # couriers_json = json.dumps(couriers)
        # return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # controller.delete_courier(courier_name)
    else:
        pass
        # return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def region(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass
        # # create a form instance and populate it with data from the request:
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # user_email = body['userEmail']
        #
        # # process the data in form.cleaned_data as required
        # # ...
        # # redirect to a new URL:
        # result = controller.safe_add_new_courier(courier_name, user_email)
        # if result['Success'] is False:
        #     if 'Duplicate courier name' in result['Message']:
        #         return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        pass
        # couriers = controller.get_all_couriers()
        # couriers_json = json.dumps(couriers)
        # return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # controller.delete_courier(courier_name)
    else:
        pass
        # return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')


@csrf_exempt
def street(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pass
        # # create a form instance and populate it with data from the request:
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # user_email = body['userEmail']
        #
        # # process the data in form.cleaned_data as required
        # # ...
        # # redirect to a new URL:
        # result = controller.safe_add_new_courier(courier_name, user_email)
        # if result['Success'] is False:
        #     if 'Duplicate courier name' in result['Message']:
        #         return HttpResponseBadRequest(result['Message'])

    elif request.method == 'GET':
        pass
        # couriers = controller.get_all_couriers()
        # couriers_json = json.dumps(couriers)
        # return HttpResponse(couriers_json, content_type="application/json")
    elif request.method == 'DELETE':
        pass
        # body_unicode = request.body.decode('utf-8')
        # body = json.loads(body_unicode)
        # courier_name = body['courierName']
        # controller.delete_courier(courier_name)
    else:
        pass
        # return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return HttpResponse('Success request')

