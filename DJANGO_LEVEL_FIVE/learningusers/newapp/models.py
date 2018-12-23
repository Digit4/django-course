from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
	"""Docstring for userprofilenfo
	"""

	user = models.OneToOneField(User, on_delete=models.PROTECT)

	# Additional class elements
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return (self.user.username)
