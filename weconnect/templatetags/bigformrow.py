from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static 

register = template.Library()

@register.filter(name='bigformrow', is_safe=True)
def bigformrow(field, name):

	#print(field.field.__class__.__name__)
	#print(field.field.widget.__class__.__name__)

	if field.field.__class__.__name__ == 'ImageField' or field.field.__class__.__name__  == 'FileField' :
		str =  '<div class="form-group">'
		str += '	<label for="' + field.id_for_label + '" class="create_project_question control-label">' + name + '</label>'
		str += '		    <div class="create_project_answers">'
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
		str += '	<label for="' + field.id_for_label + '" class="create_project_question control-label">' + name + '</label>'
		str += '		    <div class="create_project_answers">'
		str += 					field.as_widget()
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'

	elif field.field.__class__.__name__ == 'BooleanField':

		error_class = ''

		if field.errors:
			error_class = 'has-error'

		str =  '<div class="form-group ' + error_class + '">'
		str += '	<label for="' + field.id_for_label + '" class="create_project_question control-label">' + name + '</label>'
		str += '		    <div class="create_project_answers">'
		str += 					field.as_widget()
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'

	else:
		error_class = ''

		if field.errors:
			error_class = 'has-error'
		
		str =  '<div class="form-group ' + error_class + '">'
		str += '	<label for="' + field.id_for_label + '" class="create_project_question control-label">' + name + '</label>'
		str += '		    <div class="create_project_answers">'
		str += 					field.as_widget(attrs={"class":"form-control"})
		str += mark_safe(field.errors)
		str += '			</div>'
		str += '</div>'
	return mark_safe(str)