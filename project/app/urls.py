from django.conf.urls import url
from . import views


urlpatterns	= [
	url(r'^$',	views.post,	name='posts'),
	url(r'^$', views.users, name='users'),
	# url(r'^post/(?P<pk>[0-9]+)/$',	views.post_detail,	name='post_detail'),
]
