from django import forms
from django.core import validators

def checkz(value):
	if (value[0].lower() != 'z'):
		raise forms.ValidationError("Name has to start with z")

class NewForm(forms.Form):
	name = forms.CharField(validators=[checkz])
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


