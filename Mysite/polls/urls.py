from django.urls import path,re_path
from . import views

app_name='polls'

urlpatterns = [
    path('', views.index,name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.detail,name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/result/$', views.result,name='result'),
    re_path(r'^(?P<pk>[0-9]+)/vote/$', views.vote,name='vote'),
]