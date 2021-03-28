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
from django.urls import path

from introduction.views import HomePageView, ProfilePageView, KeyPageView, ThisWeekPageView, TodayPageView

urlpatterns = [
    path('home/', HomePageView),
	path('home/home/', HomePageView), #page after user presses submit
	path('', HomePageView),
    path('admin/', admin.site.urls),
    path('profile/', ProfilePageView),
    path('key/', KeyPageView),
    path('this_week/', ThisWeekPageView),
    path('today/', TodayPageView),
]
