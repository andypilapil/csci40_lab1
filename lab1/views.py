from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

def HomePageView(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return render(request, 'home.html', {'name': form.cleaned_data['name']})
	else:
		form = NameForm()
	return render(request, "home.html", {'form': form})
 
def ProfilePageView(request):
	return render(request, "profile.html", {})

def KeyPageView(request):
	return render(request, "key.html", {})

def ThisWeekPageView(request):
	return render(request, "this_week.html", {})

def TodayPageView(request):
	return render(request, "today.html", {})
