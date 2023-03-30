from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, ClearableFileInput, DateTimeField, FloatField
from django import forms
from models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','item']

class SkladForm(ModelForm):
    class Meta:
        model = Sklad
        fields = ['name', 'price', 'count', 'nikotin',\
                  'total_count', 'count_of_sold', 'info', 'img',\
                  'type','tag']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "count": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во'
            }),
            "nikotin": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Никотин'
            }),
            "total_count": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'За все время'
            }),
            "info": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "img": ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            "type": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип продукции'
            }),
            "tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Теги:'
            })
        }