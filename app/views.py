
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print("hello djangooo ttt")
    return render(request, "index.html")


def info(request):
    return HttpResponse("<p> Welcome to my django project</p>")