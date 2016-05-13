import json
import pickle

from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from flask.json import JSONEncoder

from internet_store import controller


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def user(request):
    response = HttpResponse('3AEBuCb')

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
                raise ValidationError(
                    'This e-mail is already exists: %(value)s',
                    code='duplicate',
                    params={'value': 'test@test.ru'}
                )

    elif request.method == 'GET':
        # response_data = {
        #     'users': controller.get_all_users()
        # }

        j = serializers.serialize('json', controller.get_all_users())
        #j = json.dumps(response_data)
        return HttpResponse(json.dumps(j), content_type="application/json")
    elif request.method == 'DELETE':
        pass
    else:
        return HttpResponseBadRequest('Http method ' + request.method + ' is not supported')

    return response


def courier(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        controller.delete_all_users()

    return HttpResponse('3AEBuCb')


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, unicode, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct