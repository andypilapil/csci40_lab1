from django import forms

from .models import *

class NameForm(forms.ModelForm):
	class Meta:
		model = MyModel
		fields = ['name']

class ProfileNicknameForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['profile_nickname']

class ProfileBioForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['profile_bio']

class ProfileImageForm(forms.ModelForm):
	class Meta:
		model = ProfileImageModel
		fields = ['image']

class KeyUpdateForm(forms.ModelForm):
	class Meta:
		model = KeyModel
		fields = ['key', 'key_description']

class ThisWeekUpdateForm(forms.ModelForm):
	class Meta:
		model = ThisWeekModel
		fields = ['item_type', 'item_details']

class TodayUpdateForm(forms.ModelForm):
	class Meta:
		model = TodayModel
		fields = ['item_type', 'item_details']

