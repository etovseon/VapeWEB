from django.db import models
from django.utils import timezone
from django.db import models
from django import forms
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User




class Sklad(models.Model):
    # ChoiceProductType = Product.objects.all()
    name = models.CharField('Название', max_length=50, db_index=True)
    #category = models.ForeignKey(Product, related_name='category', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    #price = models.IntegerField('Цена', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField('Кол-во')
    nikotin = models.IntegerField('Никотин мг', blank=True, null=True)
    total_count = models.IntegerField('Всего', blank=True, null=True)
    count_of_sold = models.IntegerField(default='0', blank=True, null=True)
    info = models.TextField('Доп.информация', max_length=250, blank=True, null=True)
    img = models.ImageField(upload_to='img/', null=True, blank=True, default="img/salt.jpg")
    type = models.TextField('Тип продукции', blank=True, null=True, default='Mix')
    #type = models.ForeignKey(Product, on_delete=models.CASCADE)
    #slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    model_name = 'BLiquid'
    tag = models.CharField('Теги:', max_length=200, blank=True, null=True)


class Customers(models.Model):
    phone = models.CharField(max_length=9)
    name = models.CharField(max_length=20)
    birthDay = models.CharField(max_length=10)
    chatID = models.IntegerField()
    total_amount = models.IntegerField()
    discont = models.IntegerField()
    date = models.DateTimeField()
    cachBack = models.FloatField()


class EmployerReg(models.Model):
    phone = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    date = models.DateTimeField()
    stage = models.CharField(max_length=20)
    chatID = models.IntegerField()
    findUserByID = models.IntegerField()
    role = models.IntegerField()
    report = models.IntegerField()