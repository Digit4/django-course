"""Why does module need docstrings?
"""
from django import template


register = template.Library()

def remove(value, arg):
	"""This remove out all the values of "arg" inisde your string
	"""
	return value.replace(arg, "")

register.filter('regst', register)
