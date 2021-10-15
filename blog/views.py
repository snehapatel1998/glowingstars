from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    return render(request, "portfolio.html")

def services(request):
    return render(request, "service.html")

# Create your views here.
