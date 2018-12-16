from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('main/', views.index, name='index'),
    url('get_weather/', views.get_weather, name='get_weather')
]


