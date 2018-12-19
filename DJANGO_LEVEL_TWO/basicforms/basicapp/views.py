from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index_view(request):
	return render(request, 'basicapp/index.html')

def form_view(request):
	form = forms.NewForm()
	if request.method == "POST":
		form = forms.NewForm(request.POST)

		if form.is_valid():
			# Do something
			print("Form Validation Success. Printing entered values in console")
			print("Name:%s" % form.cleaned_data['name'])
			print("Email:%s" % form.cleaned_data['email'])
			print("Text:%s" % form.cleaned_data['text'])
	return render(request, 'basicapp/form_page.html',{'form':form})
