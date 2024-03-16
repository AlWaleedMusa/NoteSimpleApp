from django.forms import ModelForm
from django import forms
from .models import Notes


class add_noteForm(ModelForm):
	class Meta:
		model = Notes
		fields = ['title', 'body']

		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
			}),
			'body': forms.Textarea(attrs={
				'class': 'form-control',
			})
		}

		labels = {
			'title': 'Note Title',
			'body': 'Note'
		}
		