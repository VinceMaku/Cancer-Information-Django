from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	index,
	about,
	types,
	Userdetail,
	UserCreate,
	Userupdate,
	Userdelete,
	)

app_name='posts'
urlpatterns = [

	url(r'^$', index, name='index'),
	url(r'^about/$', about, name='about'),
	url(r'^types$', types, name='types'),

	url(r'^questions/$', post_list, name='list'),
    url(r'^questions/create/$', post_create, name='create'),
    url(r'^questions/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^questions/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^questions/(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),

    url(r'^create/$', UserCreate, name='Create'),
    url(r'^(?P<slug>[\w-]+)/$', Userdetail, name='Userdetail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', Userupdate, name='main_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', Userdelete),
]
