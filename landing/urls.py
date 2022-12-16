from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing123/$', views.landing, name='landing'),
]
