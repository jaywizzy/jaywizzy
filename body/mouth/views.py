from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import *

# from . form import PostForm

from . form import *

# from . models import UserLogin

# Create your views here.

def post_list(request):
	
	queryset_list=Post.objects.all()#.order_by("-updated")
	paginator = Paginator(queryset_list, 5)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		#if page is out of range (eg. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list":queryset
	}

	return render(request, 'post_list.html', context)


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		jaywizzy= form.save(commit=False)
		print (form.cleaned_data.get("title"))
		print (form.cleaned_data.get("content"))
		jaywizzy.save()

		messages.success(request, "successfully created")
		return HttpResponseRedirect(jaywizzy.get_absolute_url())
	else:
		messages.error(request, "Not successfully created")
	context = {
		"form": form,
	}
	

	return render(request, 'create.html', context)


def post_view(request, id=None):
	instance = get_object_or_404(Post, id=id)
	

	context={
		"instance":instance,
		"title":instance.title
	}

	return render(request, "post_view.html", context)


def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		jaywizzy= form.save(commit=False)
		jaywizzy.save()
		
		messages.success(request, "item saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "item not saved")
	context = {
		"form": form,
		"instance":instance,
		
	}

	return render(request, 'create.html', context)


def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	# message.success("successfully deleted")
	return redirect("site:list")

def login(request):
	username = "not logged in"

	# if request.method == "POST":
	form = LoginForm(request.POST)

	if form.is_valid():
		username = form.cleaned_data['username']
		request.session['username'] = username
		messages.success(request, "successfully loggedin")

	else:
		messages.error(request, "not successfully loggedin")
		form = LoginForm()

	return render(request, 'loggedin.html', {"username" : username})

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, 'login.html', {})

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponseRedirect("/mysite/login/")
