from django.shortcuts import render
from django.http import HttpResponse
import datetime

def post_list(request):
    return render(request, 'post_list.html', {})


def post_index(request):
    html = "Hola Mundo"
    return HttpResponse(html)