from django.conf.urls import url
from django.contrib import admin
from . views import (
	post_list,
	post_create,
	post_update,
	post_view,
	post_delete,
	login,
	formView,
	logout,
	)

urlpatterns = [ 
    url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<id>\d+)/$', post_view, name="post_detail"),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'home/$', login),
    url(r'^login/',formView, name = 'loginform'),
    url(r'^logout/',logout),
]