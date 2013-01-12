from django.template import Context
from models import Topic

def show_data(request):
    """
    show all the topics
    check for optional get args
    skip all() query
    """
    data = {}
    if request.GET.get('topic', None):
        try:
            data['topic'] = Topic.objects.get(pk=int(request.GET.get('topic')))
        except Topic.DoesNotExist:
            pass
    # dont bother calling list query if were on detial page....
    if not data.get('topic'):
        data['topics'] = Topic.objects.all()

    return Context(data)

def error_data(request):
    """
    check for any errors
    """
    data = {'errors': False, 'message': None, 'result': 'ok'}

    if request.GET.get('error', 'n'):
        if request.GET.get('error', 'n') == 'y':
            data['result'] = 'error'
            data['errors'] = True

    data['result'] = request.GET.get('result', 'ok')

    if request.GET.get('message', None):
        data['message'] = request.GET.get('message', None)

    return Context(data)


