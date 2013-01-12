from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^login/', login,{'template_name': 'registration/login.html'}),
    url(r'^accounts/login/', login,{'template_name': 'registration/login.html'}),
    url(r'^logout/', logout,{'template_name': 'registration/logout.html'}),

    url(r'^show/$', 'demo.demo_app.views.view_topic', name='viewtopic'),
    url(r'^$', 'demo.demo_app.views.show_topics', name='index'),

    
    url(r'^favorites/', include('favorites.urls')),

)
