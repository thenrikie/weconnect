from django.shortcuts import render
from contacts.models import Contact
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from emails import sender
import json

# Create your views here.
def create_contact(r):

	if r.is_ajax():
		if r.method == 'POST':
			data = json.loads(r.body.decode("utf-8"))
			
			contact = Contact(email=data['email'], message=data['message'])
			contact.save()

			sender.contact_us_message({
				'email': contact.email,
				'message': contact.message
			})

			return JsonResponse({}, status=200)
	else:
		return JsonResponse({'error' : 'Only application/json content type is allowed'}, status=400);