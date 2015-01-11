from django.conf.urls import patterns, include, url
from score import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^basic-scoring/$', views.basic_scoring, name='basic_scoring'),
	url(r'^add-points/$', views.add_points, name='add_points'),
)