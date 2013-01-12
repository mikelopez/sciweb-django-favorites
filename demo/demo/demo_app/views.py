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

from models import Topic

from decimal import Decimal

import logging
logger = logging.getLogger('demo_app.views')


@login_required
def show_topics(request):
    """
    Show the topics available to favorite
    """
    return render(request, 'demo_app/show_topics.html')


@login_required
def view_topic(request):
    """
    show a specific product and include favorited info
    todo - fix template return
    """
    return render(request, 'demo_app/view_topic.html')









