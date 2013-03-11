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

def return_url(request, result):
    """
    generate the return url with the required error params
    used privately
    """
    return_url = request.REQUEST.get('next') or \
        request.META.get('HTTP_REFERER', '/')
    params = {'result': 'ok', 'message': 'Added to favorites'}
    if not result:
        if '?' in return_url:
            params['result'] = 'error'
            params['message'] = 'Could not add Favorite'
            return_url += '&%s' % urllib.urlencode(params)
        else:
            return_url += '?%s' % urllib.urlencode(params)
    return return_url, params


def get_model_object(request, model_pk, item_pk):
    """
    get the model object from ContentType pk
    """
    ctype = get_object_or_404(ContentType, pk=model_pk)
    model_class = ctype.model_class()
    obj = get_object_or_404(model_class, pk=item_pk)
    return obj


@login_required
def add_favorite(request, item, model_pk):
    """
    add a favorite for an object to a user
    return http response or an ajax json response
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    obj = get_model_object(request, model_pk, item)
    fav = Favorites.objects.get_favorite(request.user, obj)
    # add if not exist
    if not fav:
        fav = Favorites.objects.add_favorite(request.user, obj)

    returnurl, jsondata = return_url(request, fav)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))


@login_required
def remove_favorite(request, item, model_pk):
    """
    remove a favorite for an object to a user
    return http response or ajax json response
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    obj = get_model_object(request, model_pk, item)
    fav = Favorites.objects.get_favorite(request.user, obj)
    # delete the object
    if fav:
        fav.delete()

    returnurl, jsondata = return_url(request, fav)
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(jsondata), mimetype="application/json")
    return HttpResponseRedirect("%s" % (returnurl))



