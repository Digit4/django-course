from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(requests):
	help_d = {"print_here": "<h1 align=\"center\">Help Page</h1>"}
	return render(requests, "appTwo/help.html", context=help_d)

def index(request):
	return HttpResponse("<h1 clign='center'>My Second App</h1>")