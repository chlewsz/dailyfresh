# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=20, default='500g')
    gclick = models.IntegerField()
    gintro = models.CharField(max_length=200)
    grepertory = models.IntegerField()
    gdetail = HTMLField()
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle
