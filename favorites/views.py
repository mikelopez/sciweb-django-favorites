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
    """Gets the content type object """
    ctype = get_object_or_404(ContentType, pk=content_type_pk)
    model_class = ctype.model_class()
    obj = get_object_or_404(model_class, pk=item_pk)
    return obj


@login_required
def add_favorite(request, item_pk, content_type_pk):
    """ Add a favorite for an object to a user.
    Return http response or an ajax json response.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    # get the fav object - add if it doesnt exist already
    obj = get_model_object(request, content_type_pk, item_pk)
    fav = Favorites.objects.get_favorite(request.user, obj)
    if not fav:
        # add if not exist
        fav = Favorites.objects.add_favorite(request.user, obj) 

    # get the redirect-url and json data
    returnurl, jsondata = return_url(request, fav)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))


@login_required
def remove_favorite(request, item, model_pk):
    """ Remove a favorite for an object to a user.
    Return http response or ajax json response.
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    # get the object and delete it 
    obj = get_model_object(request, model_pk, item)
    fav = Favorites.objects.get_favorite(request.user, obj)
    if fav:
        # delete the object
        fav.delete()

    # set messages to override the default and get redirect-url / json data
    params = {'message': 'Removed from favorites'}
    returnurl, jsondata = return_url(request, fav, params=params)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))



