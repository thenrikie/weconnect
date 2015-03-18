from django.shortcuts import render, redirect, get_object_or_404
from pitches import forms
from pitches.models import Pitch
from datetime import datetime

# Create your views here.
def accept(r, pitch_id):
	pitch = get_object_or_404(Pitch, pk=pitch_id)


	if pitch.state != 'waiting':
		print('project not in waiting state!')
		return redirect('/')

	if  pitch.company != r.user:
		print('only company user can accept!')
		return redirect('/')

	form = forms.Accept()

	if r.method == 'POST':
		form = forms.Accept(r.POST)
		if form.is_valid():
			print("Valid form")
			pitch.desc = form.cleaned_data['desc']
			pitch.rate = form.cleaned_data['rate']
			pitch.price = form.cleaned_data['price']
			pitch.change_state('accepted')

			pitch.save()
			return redirect('/')

			
	return render(r, 'pitches/accept.html', {'pitch': pitch, 'form' : form})

def reject(r, pitch_id):

	if r.method == 'POST':
		pitch = get_object_or_404(Pitch, pk=pitch_id)

		if pitch.state != 'waiting':
			print('project not in waiting state!')
			return redirect('/')

		pitch = get_object_or_404(Pitch, pk=pitch_id)
		pitch.change_state('rejected')

		pitch.save()
		return redirect('/')

	return redirect('/')