from django.conf.urls import patterns, include, url
from home import views

urlpatterns = patterns('',
	url(r'^$', views.welcome, name='welcome'),
	url(r'^help/$', views.help, name='help'),
)