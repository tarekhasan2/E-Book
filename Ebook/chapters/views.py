from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import Chapter 
from .forms import ChapterForm
from novels.models import Novel
#from .models import get_id

from urllib.parse import urlparse, parse_qs

# Create your views here.
def chapter_details(request, id = None):

	item = get_object_or_404(Chapter ,id = id)
	last_item = Chapter.objects.filter(parent=item.parent).last()
	next_item = Chapter.objects.filter(parent=item.parent,id__gt=id).order_by('id').first()
	if(last_item == item):
		next_item = None
	print(next_item)
	# youtube = None

	# if item.video is not None:
	# 	video = item.video
	# 	u_pars = urlparse(video)
	# 	print("qq")
	# 	quer_v = parse_qs(u_pars.query).get('v')

	# 	if quer_v:
	# 		return quer_v[0]

	# 	pth = u_pars.path.split('/')
	# 	if pth:
	# 		youtube = pth[-1]
	# else:
	# 	youtube = None

	context = {
		'item' : item,
		#'youtube' : youtube
		"next_item":next_item
	}
	return render (request, "chapter_details.html", context)

def chapter_create(request, id=None):
	form = ChapterForm(request.POST or None, request.FILES or None)
	novel = get_object_or_404(Novel, id=id)
	if request.method=='POST' and 'publish' in request.POST:
		if form.is_valid():
			# data = form.cleaned_data
			# title = data['title']
			# content = data['content']
			# if Chapter.objects.filter(id=last_.id, title=title, content=content).exists():
			# 	return redirect("novels:update", id=id)
			instance = form.save(commit=False)
			instance.user = request.user
			instance.draft = False
			#instance.id = id_
			instance.parent = id
			instance.save()
			novel.drafted=False
			novel.save()
			#messages.success(request, "Seccessfully Created")
			return redirect("chapters:details", id=instance.id)
	elif request.method=='POST' and 'save' in request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.draft = True
			instance.user = request.user
			instance.parent = id
			instance.save()
			#messages.success(request, "Seccessfully Created")
			return redirect("chapters:details", id=instance.id)
	elif request.method=='POST' and 'preview' in request.POST:
		if form.is_valid():
			data = form.cleaned_data
			title = data['title']
			content = data['content']
			image = data['image']
			user = request.user
			#messages.success(request, "Seccessfully Created")
			context1 = {
				"title" : title,
				"content" : content,
				"image" : image

			}
			return render(request, "preview.html", context1)

	context = {
		#"chapter":instance,
		"form":form
	}
	
	return render (request, "chapter_create.html", context)

def chapter_update(request, id = None):
	instance  = get_object_or_404(Chapter, id=id)
	novel = get_object_or_404(Novel, id=instance.parent)
	form = ChapterForm(request.POST or None, request.FILES or None, instance=instance)
	if 'publish' in request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			#instance.parent = id
			instance.draft = False
			instance.save()
			novel.drafted = False
			novel.save()
			#messages.success(request, "Seccessfully Created")
			return redirect("chapters:details", id= instance.id)
	elif 'save' in request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.draft = True
			instance.user = request.user
			#instance.parent = id
			instance.save()
			#messages.success(request, "Seccessfully Created")
			return redirect("chapters:details", id=instance.id)
	elif 'preview' in request.POST:
		if form.is_valid():
			data = form.cleaned_data
			title = data['title']
			content = data['content']
			image = data['image']
			user = request.user
			#messages.success(request, "Seccessfully Created")
			context1 = {
				"title" : title,
				"content" : content,
				"image" : image

			}
			return render(request, "preview.html", context1)
	elif 'publish_change' in request.POST:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.draft = False
			#instance.parent = id
			instance.save()
			#messages.success(request, "Seccessfully Created")
			return redirect("chapters:details", id=instance.id)

	context = {
		"chapter":instance,
		"form":form
	}

	
	return render (request, "chapter_update.html", context)

def chapter_delete(request, id = None):
	item = get_object_or_404(Chapter, id=id)

	if request.POST:
		item.delete()

		return redirect("novels:list")
	context = {
		"item":item
	}
	
	return render (request, "chapter_delete.html", context)