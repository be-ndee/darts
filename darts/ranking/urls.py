from django.conf.urls import patterns, include, url
from ranking import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^show-profile/(?P<username>[-\w]+)$', views.show_profile, name='show_profile'),
)