from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'pages/index.html')

def index(request):
    return render(request,'pages/about.html')