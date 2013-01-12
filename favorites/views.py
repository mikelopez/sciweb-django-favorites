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

from models import Favorites

from decimal import Decimal

import logging
logger = logging.getLogger('favorites.views')

@login_required
def add_favorite(request, item, model_pk):
    """
    add a favorite for an object to a user
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirec('/login')

    ctype = get_object_or_404(ContentType, pk=model_pk)
    model_class = ctype.model_class()
    obj = get_object_or_404(model_class, pk=item)

    if not Favorites.objects.get_favorite(request.user, obj):
        fav = Favorites.objects.add_favorite(request.user, obj)
    
    return HttpResponseRedirect(request.REQUEST.get('next') or \
        request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_favorite(request, item):
    pass

