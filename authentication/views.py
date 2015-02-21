from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

class Login(View):
	def get(self, r):
		return render(r, 'auth/login.html')

	def post(self, r):
		return HttpResponse('Post');

