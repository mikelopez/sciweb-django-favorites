from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'add/(?P<item>\d+)/(?P<model_pk>\d+)$', 'favorites.views.add_favorite', name="addfavorite"),
    url(r'remove/(?P<item>\d+)/(?P<model_pk>\d+)$', 'favorites.views.remove_favorite', name="removefavorite"),
    url(r'status/(?P<object_id>\d+)/(?P<content_type>\d+)$', 'favorites.views.in_favorites', name="in_favs"),

)
