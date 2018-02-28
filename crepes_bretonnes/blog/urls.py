#-*- coding : utf8 -*-
from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
    url(r'accueil/$','blog.views.home'),
    url(r'^$',views.tpl),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
    )