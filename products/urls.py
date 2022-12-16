from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin
from products import views

urlpatterns = [
    # url(r'^landing123/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]
