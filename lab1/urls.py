from django.urls import path

from .views import *


urlpatterns = [
    path('', home_page_view, name='home'),

    path('', profile_page_view, name='profile'),

    path('', key_page_view, name='key'),
	path('', key_create, name='key_create'),
    path('', key_edit, name='key_edit'),
    path('', key_delete, name='key_delete'),

    path('', this_week_page_view, name='this week'),
	path('', this_week_create, name='this_week_create'),
    path('', this_week_edit, name='this_week_edit'),
    path('', this_week_markasdone, name='this_week_markasdone'),
    path('', this_week_delete, name='this_week_delete'),

    path('', today_page_view, name='today'),
    path('', today_create, name='today_create'),
    path('', today_edit, name='today_edit'),
    path('', today_delete, name='today_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
