from django.template import Context
from models import Topic

def show_data(request):
    """
    show all the topics
    """
    return Context({'topics': Topic.objects.all(), 'testdata': 'test'})


