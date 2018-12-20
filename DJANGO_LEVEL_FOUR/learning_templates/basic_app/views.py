from django.shortcuts import render

# Create your views here.
def index(request):
    """Displays index page, i.e. Home Page of the website.
    """
    # Context dictionary for template filter example
    context_dict = {'text':'Check this out: google.com!', 'number': 1234}
    return render(request,'basic_app/index.html', context=context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
