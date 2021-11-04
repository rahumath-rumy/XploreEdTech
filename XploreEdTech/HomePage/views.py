from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    name = "Rahmath"
    return render(request, 'index.html', {'name': name})


def signup(request):
    return render(request, 'signup.html')

#def techtool(request, home_id):
   #return HttpResponse ("<h3> This page has all the tech tools </h3>")
