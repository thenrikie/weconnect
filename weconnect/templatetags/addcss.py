from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addattrs')
def addattrs(field, attrs):
	attrdict = {}
	attrs = attrs.split(",")
	for attr in attrs:
		attr = attr.split("=")
		attrdict[attr[0]] = attr[1]

	return field.as_widget(attrs=attrdict)