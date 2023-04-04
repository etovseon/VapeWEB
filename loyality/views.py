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
        print('addIDByPost')
        print(f'{item=}')
        print(f'data: {item["data"]}\n idCustomer: {item["idCustomer"]}\n')
        key = str(item['idCustomer'])
        value = str(item['data'])
        # key = list(item.keys())[0]
        # value = item[key]
        # print(value)
        redis_instance.set(key, value)
        response = {
            'msg': f"{key} successfully set to {value}"
        }
        # print(response)
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
    return render(request, 'main2.html', {"date": date, 'customers': customers})



@csrf_exempt
def custLeft(request):
    button_value = request.GET.get('buttonValue')
    print('button2: ', button_value)
    return JsonResponse(button_value, safe=False)


@csrf_exempt
def choosenCustomer(request):
    button_value = request.GET.get('buttonValue')

    client = list(Customers.objects.filter(id=button_value).values())[0]
    print(client)
    return JsonResponse(client, safe=False)


from django.views.generic import ListView
from django.db.models import Q


class CustomerListView(ListView):
    model = Customers
    template_name = 'customer_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        if query:
            customers = Customers.objects.filter(
                Q(name__icontains=query) | Q(phone__icontains=query)
            )
            return customers
        return Customers.objects.all()


class ProductListView(ListView):
    model = Customers
    template_name = 'product_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            products = Customers.objects.filter(name__icontains=query)
            return products

        return Customers.objects.all()



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from .models import MyModel

class MyModelListView(ListView):
    model = Customers
    template_name = 'my_model_list.html'
    paginate_by = 10
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        paginator = Paginator(queryset, self.paginate_by, orphans=self.paginate_orphans)
        page = self.request.GET.get('page')
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context['paginated_queryset'] = paginated_queryset
        return context
