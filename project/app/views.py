from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .models import Post
# from .models import post

# Create your views here.
def post(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'posts.html', {'posts':posts})

def users(request):
	return render(request, 'blog.html', {})

def post_detail(request, pk):
	Post.objects.get(pk=pk)

