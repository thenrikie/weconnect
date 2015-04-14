from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os


def business(r):
	return render(r, 'weconnect/business.html')

def customer(r):
	return render(r, 'weconnect/customer.html')

def index(r):
	return customer(r)