from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    name = "Rahmath"
    return render(request, 'index.html', {'name': name})


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                print("Email already exists")
            if User.objects.filter(username=username).exists():
                print("Username already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print('user created')

        else:
            print("Passwords dont match")

        return redirect('/')
    else:
        return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')


#def techtool(request, home_id):
   #return HttpResponse ("<h3> This page has all the tech tools </h3>")
