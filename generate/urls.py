#-*- coding:utf-8

from django.conf.urls import include, url
from generate import views

urlpatterns=[
    url(r'$',views.index),

]