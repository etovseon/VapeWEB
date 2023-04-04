from django.shortcuts import render
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .apiLogic import *
# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)


def func_name_hi(func):
    def wrapper(*args, **kwargs):
        print(f'Hi i`m {func.__name__}')
        func(*args, **kwargs)
    return wrapper


@csrf_exempt
@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        return api_get()
    elif request.method == 'POST':
        return api_post(request)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        return api_getV2(**kwargs)
    elif request.method == 'PUT':
        return api_put(request, **kwargs)
    elif request.method == 'DELETE':
        return api_delete(**kwargs)


@csrf_exempt
@api_view(['POST','GET'])
def customerOrderAPI(request, *args, **kwargs):
    if request.method == 'POST':
        return api_customerOrder(request, **kwargs)
