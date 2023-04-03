from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', main, name=''),
    path('get-id/', addIDByPost, name='get-id'),
    path('get-customer/', getCustomer, name='get-customer'),
    path('cust/', choosenCustomer, name='choosenCustomer'),
    path('custLeft/', custLeft, name='custLeft'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('mu-model-list/', MyModelListView.as_view(), name='my_model_list'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)