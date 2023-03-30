from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    path('', main, name=''),
    path('get-id/', addIDByPost, name='get-id'),
    path('get-customer/', getCustomer, name='get-customer'),
    path('cust/', choosenCustomer, name='choosenCustomer')
}
# urlpatterns = format_suffix_patterns(urlpatterns)