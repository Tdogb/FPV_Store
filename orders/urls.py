from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^cart$', views.cart, name='cart'),
]