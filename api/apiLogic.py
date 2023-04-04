from django.shortcuts import render
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)


def api_get():
    items = {}
    count = 0
    for key in redis_instance.keys("*"):
        items[key.decode("utf-8")] = redis_instance.get(key)
        count += 1
    response = {
        'count': count,
        'msg': f"Found {count} items.",
        'items': items
    }
    return Response(response, status=200)


def api_getV2(**kwargs):
    if kwargs['key']:
        value = redis_instance.get(kwargs['key'])
        if value:
            response = {
                'key': kwargs['key'],
                'value': value,
                'msg': 'success'
            }
            return Response(response, status=200)
        else:
            response = {
                'key': kwargs['key'],
                'value': None,
                'msg': 'Not found'
            }
            return Response(response, status=404)


def api_post(request):
    item = json.loads(request.body)
    key = list(item.keys())[0]
    value = item[key]
    redis_instance.set(key, value)
    response = {
        'msg': f"{key} successfully set to {value}"
    }
    return Response(response, 201)


def api_put(request, **kwargs):
    if kwargs['key']:
        request_data = json.loads(request.body)
        new_value = list(request_data.values())[0]
        value = redis_instance.get(kwargs['key'])
        if value:
            redis_instance.set(kwargs['key'], new_value)
            response = {
                'key': kwargs['key'],
                'pre value': value,
                'new value': new_value,
                'msg': f"Successfully updated {kwargs['key']}"
            }
            return Response(response, status=200)
        else:
            response = {
                'key': kwargs['key'],
                'value': None,
                'msg': 'Not found'
            }
            return Response(response, status=404)


def api_delete(**kwargs):
    if kwargs['key']:
        result = redis_instance.delete(kwargs['key'])
        if result == 1:
            response = {
                'msg': f"{kwargs['key']} successfully deleted"
            }
            return Response(response, status=404)
        else:
            response = {
                'key': kwargs['key'],
                'value': None,
                'msg': 'Not found'
            }
            return Response(response, status=201)


def decorFuncName(func):
    def wrapper(*args, **kwargs):
        print('*'*30)
        print(f' • Response func: [{func.__name__}]')
        return func(*args, **kwargs)
    return wrapper

@decorFuncName
def api_customerOrder(request):
    result = request.body.decode('utf-8')
    result = json.loads(result)
    print(f"Order items: {result['data']}")
    print(f"CustomerID: {result['idCustomer']}")
    response = 'ok'
    return Response(response, status=201)