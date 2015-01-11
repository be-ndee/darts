from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'darts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^user/', include('user_management.urls', namespace='user')),
    url(r'^score/', include('score.urls', namespace='score')),
)
