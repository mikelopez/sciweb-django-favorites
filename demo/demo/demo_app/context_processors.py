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


