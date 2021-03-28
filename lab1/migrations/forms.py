from django import forms

class NameForm(forms.Form):
	name = forms.CharField(label='Enter your name here', max_length=100)