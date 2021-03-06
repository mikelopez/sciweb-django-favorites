import time
import os
import mimetypes
import simplejson
from datetime import datetime, timedelta

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse, resolve
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.contenttypes.models import ContentType
import urllib

from models import Favorites

from decimal import Decimal

import logging
logger = logging.getLogger('favorites.views')

def return_url(request, result, params=None):
    """ The return URL is where the user is taken if the
    request (add-fav / remove-fav) was made via post or any other non ajax.
    Generate the return url with any get params.
    
    Used privately via add_favorite / remove_favorite
    
    Parameters params: Send a dict with any key(s) you would want
    to replace from default_params. Any keys that are not passed
    but available in default_params will be set 
    with the default values.

    """
    return_url = request.REQUEST.get('next') or \
        request.META.get('HTTP_REFERER', '/')
    default_params = {'result': 'ok', 'message': '200 ok'}

    if not params:
        params = default_params
    for k, v in default_params.items():
        if not k in params.keys():
            params[k] = v

    if not result:
        if '?' in return_url:
            params['result'] = 'error'
            params['message'] = 'Could not add Favorite'
            return_url += '&%s' % urllib.urlencode(params)
        else:
            return_url += '?%s' % urllib.urlencode(params)
    return return_url, params


def get_model_object(request, content_type_pk, item_pk):
    """First gets the content_type object, and gets the model_class
    to then search by item_pk to get the model_class instance
    of the favorite object if any."""
    try:
        ctype = ContentType.objects.get(pk=content_type_pk)
        model_class = ctype.model_class()
        try:
            #fav_item = get_object_or_404(model_class, pk=item_pk)
            fav_item = model_class.objects.get(pk=item_pk)
        except model_class.DoesNotExist:
            return False
        return fav_item
            #ctype = get_object_or_404(ContentType, pk=content_type_pk)
    except ContentType.DoesNotExist:
        return False
    


@login_required
def add_favorite(request, item_pk, content_type_pk):
    """ Add a favorite for an object to a user.
    Return http response or an ajax json response.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    jsondata = {}
    # get the fav object - add if it doesnt exist already
    fav_item = get_model_object(request, content_type_pk, item_pk)
    if fav_item:
        # add if not exist
        fav = Favorites.objects.add_favorite(request.user, fav_item) 
        # get the redirect-url and json data
        returnurl, jsondata = return_url(request, fav)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))


@login_required
def remove_favorite(request, item_pk, content_type_pk):
    """ Remove a favorite for an object to a user.
    Return http response or ajax json response.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    # get the object and delete it 
    jsondata = {}
    fav_item = get_model_object(request, content_type_pk, item_pk)
    if fav_item:
        fav = Favorites.objects.get_favorite(request.user, fav_item)
        if fav:
            # delete the object
            fav.delete()

        # set messages to override the default and get redirect-url / json data
        params = {'message': 'Removed from favorites'}
        returnurl, jsondata = return_url(request, fav, params=params)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))


@login_required
def in_favorites(request, object_id, content_type):
    """Checks if it is in favorites."""
    fav_item = get_model_object(request, content_type, object_id)
    fav = Favorites.objects.get_favorite(request.user, fav_item)
    if fav:
        data = {"in_favorites": True}
    else:
        data = {"in_favorites": False}
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")



