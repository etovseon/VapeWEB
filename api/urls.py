from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    path('items/', manage_items, name="items"),
    path('items/<slug:key>', manage_item, name="single_item"),
    path('customerOrderAPI/', customerOrderAPI, name='customerOrder_API'),
}
urlpatterns = format_suffix_patterns(urlpatterns)