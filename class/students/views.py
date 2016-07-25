from django.shortcuts import render

from django.http import HttpResponse

from nhub.models import Users

from django.http import HttpResponseRedirect

from.form import Contactus

from.form import Articleposts

from.form import LoginForm
# from .models import *
from students.models import Contact
from students.models import Articles
from django.core.urlresolvers import reverse
# from students.models import Contact

# Create your views here.
def article(request):
	# posts=Articles.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# if request.method=='POST':
	# 	form=Articleposts(request.POST)
	# 	if form.is_valid():
	# 		return HttpResponseRedirect('/babayaga/')
	# else:
	# 	form=Articleposts()
	return render (request, 'article.html', {})

def deletes(request,id):
	
	Contact.objects.filter(id=id).delete()
	return HttpResponseRedirect('/info/')

	#print(segun)
	#print(request.GET['id'])

	# return render (request, 'delete.html', {'segun':id})
def view(request,id):
	esse = id
	display= Contact.objects.get(id=esse)
	return render(request, 'view.html', {'segun':id,'display':display})

def edit(request,id):
	segun = id
	# display=Contact.objects.get('name'='omobolaji')

	return render(request, 'edit.html', {'segun':id})
def wizzy(request):
	if request.method=='POST':
		form=Contactus(request.POST)
		if form.is_valid():
			a=form.cleaned_data['name']
			b=form.cleaned_data['subject']
			c=form.cleaned_data['message']
			d=form.cleaned_data['email']
			Contact.objects.create(name=a, subject=b, message=c, email=d)

			return HttpResponseRedirect('/info/')
	else:
		form=Contactus()
		return render (request, 'index_contact.html', {'form': form})
def dam(request):
	display=Contact.objects.all()
	return render (request, 'contact.html',{"table":display})

def junior(request):
	return HttpResponse("<body style='background-color:orange'> whad up fellas</body>")
def olu(request):
	return render(request, 'index.html', {})
	# k= Users.objects.get(first_name="jay").first_name
	# wiz='''
	# 		<html>
	# 			<body style="background-color:gray">
	# 					<p>%s</p>

	# 			</body>
	# 		</html>

	# 	'''%Users
	# return HttpResponse(wiz)

def songs(request):
	return render (request, 'music.html', {})
def vids(request):
	return render (request, 'videos.html', {})
def game(request):
	return render (request, 'games.html', {})
def imgs(request):
	return render (request, 'imgs.html', {})

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'login.html', {"username" : username})
	
# def	post_list(request):
# 	return	render(request,	'blog/post_list.html',	{})