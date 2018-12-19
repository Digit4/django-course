from django import forms
from django.core import validators

def checkz(value):
	if (value[0].lower() != 'z'):
		raise forms.ValidationError("Name has to start with z")

class NewForm(forms.Form):
	name = forms.CharField(validators=[checkz])
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter your email again')
	text = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		v_mail = all_clean_data["verify_email"]
		if (email != v_mail):
			raise forms.ValidationError("emails do not match")
