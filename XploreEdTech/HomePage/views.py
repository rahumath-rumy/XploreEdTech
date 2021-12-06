from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm


def home(request):
    name = "Rahmath"
    return render(request, 'index.html', {'name': name})


def signup(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #when commented data gets updated to the db
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created!'+ user)

            return redirect('profile')

    context = {'form': form}
    return render(request, 'signup.html', context)

    #     reg = RegUser()
    #
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     reg.email = email
    #     reg.username = username
    #     reg.password = password1
    #     reg.save()
    #     return HttpResponse("thanks")
    # return render(request, 'index.html')
    #     user = User.objects.create_user(email=email, username=username, password1=password1)
    #     user.save();
    #     print("user created")
    #     return redirect('/')
    #
    # else:
    #     return render(request, 'signup.html')

        #    username = request.POST['username']
    #    email = request.POST['email']
    #     password = request.POST['password']
    #     confirmpassword = request.POST['confirmpassword']
    #
    #     if password == confirmpassword:
    #         if User.objects.filter(email=email).exists():
    #             print("Email already exists")
    #         if User.objects.filter(username=username).exists():
    #             print("Username already exists")
    #         else:
    #             user = User.objects.create_user(username=username, email=email, password=password)
    #             user.save()
    #             print('user created')
    #
    #     else:
    #         print("Passwords dont match")
    #
    #     return redirect('/')
    # else:


def profile(request):
    return render(request, 'profile.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.info(request, "The username or password entered is incorrect! Please try again!")
    context = {}
    return render(request, 'login.html', context)



def logoutuser(request):
    return redirect('login')

#def techtool(request, home_id):
   #return HttpResponse ("<h3> This page has all the tech tools </h3>")
