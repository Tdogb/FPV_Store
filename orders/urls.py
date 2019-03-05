from django.conf.urls import url, include
from . import views
from oscar.app import application

app_name = 'orders'

urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^order-list/$', views.orderList, name='order-list'),
]