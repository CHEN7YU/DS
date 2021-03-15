from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("<h1>hello world</h1>")

def about_page(request):
    return render(request,"hello_world.html")