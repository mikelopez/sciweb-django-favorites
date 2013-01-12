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
    * hardcoded url until urls & views are implemented *
    todo - handle exception
    """
    return "/favorites/add/%s/%s" % (obj.pk, ContentType.objects.get_for_model(obj).pk)



