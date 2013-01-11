from django import template
from django.contrib.contenttypes.models import ContentType 
from djano.contrib.urlresolvers import reverse

register = template.Library()

@register.filter
def get_fav(obj, user):
    """
    get the favorite on an object (obj) for a user (user)
    """
    try:
        fav = obj.objects.get_favorite(obj, user)
    except obj.DoesNotExist:
        fav = None
    return fav

@register.filter
def check_favorite(user, obj):
    """
    check if the user has already favorited
    ( user|check_favorite:item )
    """
    return get_fav()


