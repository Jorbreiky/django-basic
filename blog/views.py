from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import datetime
from django.utils import timezone

from .models import Post
from .forms import PostForm


def login(request):
	return render(request, 'login.html', {})

def page_not_found(request):
	return render(request, 'page_not_found.html', {})

def test(request):
	return render(request, 'test.html', {})

def post_all(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts = Post.objects.all().order_by('published_date')
	context = {"posts": posts}
	return render(request, "post_all.html", context)

def post_add(request):
	form = PostForm()
	return render(request, 'post_add.html', {'form': form})

def post_insert(request):
	if request.method == "POST":
		form = PostForm(request.POST)
	else:
		form = PostForm()

	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.published_date = timezone.now()
		post.save()
	return redirect('post_all', pk=post.pk)


def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_edit.html', {'post': post})

def post_index(request):
    html = "Hola Mundo"
    return HttpResponse(html)