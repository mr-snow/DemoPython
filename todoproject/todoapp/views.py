from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "home.html")


def index(request):
    return HttpResponse("hello world")
