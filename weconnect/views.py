from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from projects import forms
import os


def business(r):
	if r.user.is_authenticated() and r.user.is_admin:
		return redirect('/admin')
	elif r.user.is_authenticated() and r.user.is_customer:
		return redirect('home_customer')
	elif r.user.is_authenticated() and r.user.is_company:
		return redirect('pitches:list')

	form = forms.BusinessIndex()
	return render(r, 'weconnect/business.html', { 'form': form, 'role': 'business'})

def customer(r):
	if r.user.is_authenticated() and r.user.is_admin:
		return redirect('/admin')
	elif r.user.is_authenticated() and r.user.is_company:
		return redirect('home_business')

	form = forms.Business()
	return render(r, 'weconnect/customer.html', { 'form': form, 'role': 'customer'})

def index(r):
	if r.user.is_authenticated() and r.user.is_admin:
		return redirect('/admin')
	return customer(r)


def index_redirect(r):
	if r.user.is_authenticated() and r.user.is_admin:
		return redirect('/admin')
	return redirect('home_index')