from django.urls import path

from .views import HomePageView, ProfilePageView, KeyPageView, ThisWeekPageView, TodayPageView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('', ProfilePageView, name='profile'),
    path('', KeyPageView, name='key'),
    path('', ThisWeekPageView, name='this week'),
    path('', TodayPageView, name='today'),
]
