from django import template

register = template.Library()

@register.filter
def filename(path):
	path = path.split("/")
	return path[-1]