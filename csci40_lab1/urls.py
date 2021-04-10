"""csci40_lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView

from lab1.views import *

urlpatterns = [
    path('home/', home_page_view),
	path('home/home/', home_page_view), #page after user presses submit
	path('', home_page_view),
    path('admin/', admin.site.urls),

    path('profile/', profile_page_view),

    path('key/', key_page_view),
    path(r'key/create/$', key_create, name='key_create'),
    path(r'^key/(?P<pk>\d+)/edit/$', key_edit, name='key_edit'),
    path(r'^key/(?P<pk>\d+)/delete/$', key_delete, name='key_delete'),

    path('this_week/', this_week_page_view),
    path(r'this_week/create/$', this_week_create, name='this_week_create'),
    path(r'^this_week/(?P<pk>\d+)/edit/$', this_week_edit, name='this_week_edit'),
    path(r'^this_week/(?P<pk>\d+)/markasdone/$', this_week_markasdone, name='this_week_markasdone'),
    path(r'^this_week/(?P<pk>\d+)/delete/$', this_week_delete, name='this_week_delete'),

    path('today/', today_page_view),
    path(r'today/create/$', today_create, name='today_create'),
    path(r'^today/(?P<pk>\d+)/edit/$', today_edit, name='today_edit'),
    path(r'^today/(?P<pk>\d+)/delete/$', today_delete, name='today_delete'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)