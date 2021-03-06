from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'storages/check', views.storages_check, name='storages_check'),
    url(r'check', views.check, name='check'),
    url(r'storages', views.storages, name='storages'),
]