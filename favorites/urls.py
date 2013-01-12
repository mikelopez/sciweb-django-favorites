from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',

    url(r'add/(?P<item>\d+)/(?P<model_pk>\d+)$', 'favorites.views.add_favorite', name="add-favorite"),
    url(r'remove/(?P<item>\d+)$', 'favorites.views.remove_favorite', name="remove-favorite"),

)
