from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello...")

def contact(request):
    return HttpResponse("Contact Page")

def about(request):
    return HttpResponse("About Page")

def blog(request):
    return HttpResponse("First Blog...")