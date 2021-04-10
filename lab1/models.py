from django.db import models
from PIL import Image
from model_utils import Choices
 
# Create your models here.
class MyModel(models.Model):
	name = models.CharField(max_length=50)

class ProfileModel(models.Model):
	profile_nickname = models.CharField(max_length=20)
	profile_bio = models.CharField(max_length=100)

class ProfileImageModel(models.Model):
	image = models.ImageField(upload_to="media")

class KeyModel(models.Model): 
	key = models.CharField(max_length=20)
	key_description = models.CharField(max_length=50)

class ThisWeekModel(models.Model):
	ITEM_TYPES = Choices('Task', 'Event', 'Note')
	item_type = models.CharField(choices=ITEM_TYPES, max_length=20, blank=True, null=True)
	item_details = models.CharField(max_length=50)

class TodayModel(models.Model):
	ITEM_TYPES = Choices('Task', 'Event', 'Note')
	item_type = models.CharField(choices=ITEM_TYPES, max_length=20, blank=True, null=True)
	item_details = models.CharField(max_length=50)