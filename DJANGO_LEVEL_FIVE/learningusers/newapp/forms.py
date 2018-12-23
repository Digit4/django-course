from django import forms
from django.contrib.auth.models import User
from newapp.models import UserProfileInfo

# forms go here

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ['username', 'password', 'email']

class UserProfileInfoForm(forms.ModelForm):

	class Meta():
		model = UserProfileInfo
		fields = ['portfolio_site', 'profile_pic']
