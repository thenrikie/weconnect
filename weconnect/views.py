from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os

def index(r):
	return render(r, 'weconnect/index.html')