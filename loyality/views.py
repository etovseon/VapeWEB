from django.shortcuts import render
import requests
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework.response import Response
import redis
from django.conf import settings


@csrf_exempt
def addIDByPost(request):
    if request.method == 'POST':
        redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                           port=settings.REDIS_PORT, db=0)

        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        print(value)
        redis_instance.set(key, value)
        response = {
            'msg': f"{key} successfully set to {value}"
        }
        print(response)
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'error'})


@csrf_exempt
def getID(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for id, valueID in data.items():
            print(valueID)
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'error'})


@csrf_exempt
def getCustomer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for id, valueID in data.items():
            print('customer:', valueID)
        return valueID
    else:
        return JsonResponse({'result': 'error'})

@csrf_exempt
def main(request):
    date = Sklad.objects.filter()
    customers = Customers.objects.filter()
    js = {'kot': {'name': 'oleg', 'phone': '0978914311'}}
    return render(request, 'main2.html', {"date": date, 'customers': customers, 'js':js})


@csrf_exempt
def choosenCustomer(request):
    button_value = request.GET.get('buttonValue')
    clientDB = Customers.objects.filter(id=button_value)
    client = list(Customers.objects.filter(id=button_value).values())[0]
    # return JsonResponse({'result': button_value})
    # print(client.name)
    # clientJSON = {'name': str(client.name), 'phone':client.phone}
    # return JsonResponse(clientJSON)
    return JsonResponse(client, safe=False)
    # return Response(client)
    # return client
