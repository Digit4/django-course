from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from newapp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'newapp/home.html')


def register_view(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print("FORMS INVALID")
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
		print("POST method now working")
	return	render(request, 'newapp/registration.html', {'user_form':user_form, 'profile_form':profile_form,'registered':registered})


def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if (user.is_active):
				login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponse("Account not active")

		else:
			print("Someone tried to login and failed, if you want, here's username=%s and password=%s" % (username, password))
			return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
	return render(request, 'newapp/user_login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
	return HttpResponse("YOU ARE LOGGED IN, NICE!")
