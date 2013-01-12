from django import template
from django.contrib.contenttypes.models import ContentType 
from django.core.urlresolvers import reverse
from favorites.models import Favorites

register = template.Library()

@register.filter
def get_fav(obj, user):
    """
    get the favorite on an object (obj) for a user (user)
    """
    fav_obj = Favorites.objects.get_favorite(user, obj)
    return fav_obj


@register.filter
def check_favorite(user, obj):
    """
    check if the user has already favorited
    ( user|check_favorite:item )
    """
    return get_fav(obj, user)


@register.filter
def favorite_object(user, obj):
    """
    generate an ad link, the ordering of args matters
    user|favorite_object:topic
    """
    return "/favorites/add/%s/%s" % (obj.pk, ContentType.objects.get_for_model(obj).pk)


@register.filter
def unfavorite_object(user, obj):
    """
    generate an ad link, the ordering of args matters
    user|favorite_object:topic
    """
    return "/favorites/remove/%s/%s" % (obj.pk, ContentType.objects.get_for_model(obj).pk)


@register.filter
def my_favorites(user):
    """
    return all the users favorites
    """
    fav = Favorites.objects.filter(user=user)
    favs = []
    for i in fav:
        ctype_name = ContentType.objects.get_for_model(i.content_object).name
        favs.append({'favorite_object': ctype_name, 'obj': i.content_object})
    return favs

