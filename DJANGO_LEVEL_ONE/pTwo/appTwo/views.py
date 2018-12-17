from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
	return HttpResponse("<h1><strong>My Second App</strong></h1>")