from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	my_dict = {'insert_me': "Hello I'm from views.py!"}
	return render(request,'hello_world_app/index.html',context=my_dict)