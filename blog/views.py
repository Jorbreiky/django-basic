from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
import datetime
from django.utils import timezone

def login(request):
	return render(request, 'login.html', {})

def page_not_found(request):
	return render(request, 'page_not_found.html', {})

def post_list(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all().order_by('published_date')
	context = {"posts": posts}
	return render(request, "post_list.html", context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post.html', {'post': post})

def post_index(request):
    html = "Hola Mundo"
    return HttpResponse(html)