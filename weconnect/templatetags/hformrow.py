from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static 

register = template.Library()

@register.filter(name='hformrow', is_safe=True)
def hformrow(field, name):

	#print(field.field.__class__.__name__)
	#print(field.field.widget.__class__.__name__)

	if field.field.__class__.__name__ == 'ImageField':
		str =  '<div class="form-group">'
		str += '	<label for="' + field.id_for_label + '" class="col-sm-3 control-label">' + name + '</label>'
		str += '		    <div class="col-sm-9">'
		str += '					<input type="file" name="' + field.html_name + '" id="' + field.id_for_label + '">'
		if field.value():
			str += '					<img src="' + static(field.value().name) + '" class="image_edit">'
			str += '					<input type="checkbox" name="' + field.html_name + '-clear"> Remove '
		
		str += '			</div>'
		str += '</div>'
	elif field.field.__class__.__name__ == 'ModelMultipleChoiceField' or field.field.widget.__class__.__name__ == 'RadioSelect':

		error_class = ''

		if field.errors:
			error_class = 'has-error'
		
		str =  '<div class="form-group ' + error_class + '">'
		str += '	<label for="' + field.id_for_label + '" class="col-sm-3 control-label">' + name + '</label>'
		str += '		    <div class="col-sm-9">'
		str += 					field.as_widget()
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'

	elif field.field.__class__.__name__ == 'BooleanField':

		error_class = ''

		if field.errors:
			error_class = 'has-error'

		str =  '<div class="form-group ' + error_class + '">'
		str += '	<label for="' + field.id_for_label + '" class="col-sm-3 control-label">' + name + '</label>'
		str += '		    <div class="col-sm-9">'
		str += 					field.as_widget()
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'

	else:
		error_class = ''

		if field.errors:
			error_class = 'has-error'
		
		str =  '<div class="form-group ' + error_class + '">'
		str += '	<label for="' + field.id_for_label + '" class="col-sm-3 control-label">' + name + '</label>'
		str += '		    <div class="col-sm-9">'
		str += 					field.as_widget(attrs={"class":"form-control"})
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'
	return mark_safe(str)