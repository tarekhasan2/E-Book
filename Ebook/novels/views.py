from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Novel
from .forms import NovelCreate
from chapters.models import Chapter
from django import template
from django.template.loader import get_template 

def novels(request):
	query_set = Novel.objects.all()

	context={
		"query_set" :query_set,
	
	}

	return render (request, "novels.html", context)


def novel_details(request, id=None):
	item = get_object_or_404(Novel, id=id)
	chapters = Chapter.objects.filter(parent = id)
	context={
		"item" :item,
		"chapters" : chapters,
	}
	
	return render (request, "novel_details.html", context)
def novel_create(request):
	form = NovelCreate(request.POST or None, request.FILES or None)

	# if Chapter.objects.all() != None:
	# 	obj=Chapter.objects.last()
	# 	new_chap = obj.id+1



	form.fields['title'].required  = False
	form.fields['tags'].required  = False
	form.fields['description'].required = False
	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		form.save_m2m()
		return redirect("chapters:create" ,id=instance.id)

	context = {
		"form" : form
	}
	return render (request, "novel_create.html", context)

def novel_update(request, id=None):
	instance = get_object_or_404(Novel, id=id)
	chapter = Chapter.objects.last()
	form = NovelCreate(request.POST or None, request.FILES or None, instance=instance)
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.draft = False
		instance.user = request.user
		instance.save()
		form.save_m2m()
		return redirect("chapters:details", id=chapter.id)
	
	context = {
			#"chapter" : chapter,
	
			"form":form
		}

	return render(request, "novel_update.html", context)

def novel_update_and_content(request, id=None):
	instance = get_object_or_404(Novel, id= id)
	chapters = Chapter.objects.filter(parent=id)
	form = NovelCreate(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("novels:update_content", id=instance.id)
	context = {
		"chapters":chapters,
		"instance":instance,
		"form":form
		
	}
	return render(request, "novel_update_and_content.html", context)





def novel_delete(request , id=None):
	item = get_object_or_404(Novel , id=id)
	if request.POST:
		item.delete()
		return redirect("novels:list")
	
	context = {
		"item":item
	}
	return render (request, "novel_delete.html")
	

	



