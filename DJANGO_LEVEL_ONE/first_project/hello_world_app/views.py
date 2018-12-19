from django.shortcuts import render
from django.http import HttpResponse
from hello_world_app.models import Topic, AccessRecord, WebPage

# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(request, 'hello_world_app/index.html', context=date_dict)
