"""class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.utils import timezone

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nhub/[a-z]+/$', "nhub.views.jay"),
    url(r'^nhub/[0-9]+/$', "nhub.views.junior"),
    url(r'^nhub/[A-Z]+/$', "nhub.views.shergzie"),
    url(r'^paga/$', "students.views.junior"),
    url(r'^babayaga/$', "students.views.olu"),
    url(r'^music/$', "students.views.songs"),
    url(r'^videos/$', "students.views.vids"),
    url(r'^games/$', "students.views.game"),
    url(r'^images/$', "students.views.imgs"),
    url(r'^contactus/$', "students.views.wizzy"),
    url(r'^info/$', "students.views.dam"),
    url(r'^view/(?P<id>\d+)/$', "students.views.view", name="show"),
    url(r'^edit/(?P<id>\d+)/$', "students.views.edit", name="editing"),
    url(r'^delete/(?P<id>\d+)/$', "students.views.deletes", name="wizzo"),
    url(r'^articles/$', "students.views.article"),
    url(r'^login/$', "students.views.login"),

    

                            


    
]
