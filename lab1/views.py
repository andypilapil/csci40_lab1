
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

def home_page_view(request):
	obj=None
	form = NameForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			new_name = form.save()
			name_id = new_name.id
			obj = MyModel.objects.get(id=name_id)
	context = {
		'form': form,
		'obj': obj,
	}
	return render(request, 'home.html', context)

def profile_page_view(request):
	nickname_obj=None
	bio_obj=None
	image_obj=None
	nickname_form = ProfileNicknameForm(request.POST or None)
	bio_form = ProfileBioForm(request.POST or None)
	image_form = ProfileImageForm(request.POST, request.FILES)
	if request.method == 'POST':
		if nickname_form.is_valid():
			new_nickname = nickname_form.save()
			nickname_id = new_nickname.id
			nickname_obj = ProfileModel.objects.get(id=nickname_id)
		if bio_form.is_valid():
			new_bio = bio_form.save()
			bio_id = new_bio.id
			bio_obj = ProfileModel.objects.get(id=bio_id)
		if image_form.is_valid():
			image_form.save()
			image_obj = ProfileImageModel.objects.get(id=1)
	context = {
		'nickname_form': nickname_form,
		'bio_form': bio_form,
		'image_form': image_form,
		'nickname_obj': nickname_obj,
		'bio_obj': bio_obj,
		'image_obj': image_obj
	} 
	return render(request, "profile.html", context)

def key_page_view(request):
	obj = KeyModel.objects.all()
	return render(request, 'key.html', {'obj':obj})

def save_key_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            obj = KeyModel.objects.all()
            data['html_list'] = render_to_string('key_partial.html', {
                'obj': obj
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def key_create(request):
    if request.method == 'POST':
        form = KeyUpdateForm(request.POST)
    else:
        form = KeyUpdateForm()
    return save_key_form(request, form, 'key_create.html')

def key_edit(request, pk):
    key = get_object_or_404(KeyModel, pk=pk)
    if request.method == 'POST':
        form = KeyUpdateForm(request.POST, instance=key)
    else:
        form = KeyUpdateForm(instance=key)
    return save_key_form(request, form, 'key_edit.html')

def key_delete(request, pk):
    key = get_object_or_404(KeyModel, pk=pk)
    data = dict()
    if request.method == 'POST':
        key.delete()
        data['form_is_valid'] = True
        obj = KeyModel.objects.all()
        data['html_list'] = render_to_string('key_partial.html', {
            'obj': obj
        })
    else:
        context = {'key': key}
        data['html_form'] = render_to_string('key_delete.html', context, request=request)
    return JsonResponse(data)

def this_week_page_view(request):
	obj = ThisWeekModel.objects.all()
	return render(request, 'this_week.html', {'obj':obj})

def save_this_week_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			obj = ThisWeekModel.objects.all()
			data['html_list'] = render_to_string('this_week_partial.html', {
				'obj': obj
            })
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def this_week_create(request):
    if request.method == 'POST':
        form = ThisWeekUpdateForm(request.POST)
    else:
        form = ThisWeekUpdateForm()
    return save_this_week_form(request, form, 'this_week_create.html')

def this_week_edit(request, pk):
    item = get_object_or_404(ThisWeekModel, pk=pk)
    if request.method == 'POST':
        form = ThisWeekUpdateForm(request.POST, instance=item)
    else:
        form = ThisWeekUpdateForm(instance=item)
    return save_this_week_form(request, form, 'this_week_edit.html')

def this_week_markasdone(request, pk):
    item = get_object_or_404(ThisWeekModel, pk=pk)
    data = dict()
    if request.method == 'POST':
	    item.item_type == 'Task Done'
	    item.save()
	    data['form_is_valid'] = True
	    obj = ThisWeekModel.objects.all()
    context = {
    	'item': item,
    	'obj': obj
    }
    data['html_list'] = render_to_string('this_week_partial.html', context, request=request)
    return JsonResponse(data)

def this_week_delete(request, pk):
	item = get_object_or_404(ThisWeekModel, pk=pk)
	data = dict()
	if request.method == 'POST':
		item.delete()
		data['form_is_valid'] = True
		obj = ThisWeekModel.objects.all()
		data['html_list'] = render_to_string('this_week_partial.html', {
			'obj': obj
        })
	else:
		context = {'item': item}
		data['html_form'] = render_to_string('this_week_delete.html', context, request=request)
	return JsonResponse(data)

def today_page_view(request):
	obj = TodayModel.objects.all()
	return render(request, 'today.html', {'obj':obj})

def save_today_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			obj = TodayModel.objects.all()
			data['html_list'] = render_to_string('today_partial.html', {
				'obj': obj
            })
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def today_create(request):
    if request.method == 'POST':
        form = TodayUpdateForm(request.POST)
    else:
        form = TodayUpdateForm()
    return save_today_form(request, form, 'today_create.html')

def today_edit(request, pk):
    item = get_object_or_404(TodayModel, pk=pk)
    if request.method == 'POST':
        form = TodayUpdateForm(request.POST, instance=item)
    else:
        form = TodayUpdateForm(instance=item)
    return save_today_form(request, form, 'today_edit.html')

def today_delete(request, pk):
	item = get_object_or_404(TodayModel, pk=pk)
	data = dict()
	if request.method == 'POST':
		item.delete()
		data['form_is_valid'] = True
		obj = TodayModel.objects.all()
		data['html_list'] = render_to_string('today_partial.html', {
			'obj': obj
        })
	else:
		context = {'item': item}
		data['html_form'] = render_to_string('today_delete.html', context, request=request)
	return JsonResponse(data)
