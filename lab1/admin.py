from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MyModel)
admin.site.register(ProfileImageModel)
admin.site.register(KeyModel)
admin.site.register(ThisWeekModel)
admin.site.register(TodayModel)