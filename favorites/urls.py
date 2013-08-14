from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'add/(?P<item>\d+)/(?P<model_pk>\d+)$', 'favorites.views.add_favorite', name="addfavorite"),
    url(r'remove/(?P<item>\d+)/(?P<model_pk>\d+)$', 'favorites.views.remove_favorite', name="removefavorite"),

)
