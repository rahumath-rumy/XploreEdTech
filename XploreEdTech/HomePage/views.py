from django.shortcuts import render, redirect
from .forms import CreateUserForm, FileUpload
from django.contrib import messages
from .models import *
from .models import Worksheets
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file


def home(request):
    # name = "Rahmath"
    return render(request, 'index.html')


def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # when commented data gets updated to the db
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created!' + user)

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


@login_required(login_url='login')
def profile(request):
    prof = Profile.objects.all()
    return render(request, 'profile.html',
                  {'prof': prof})


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
    logout(request)
    return redirect('http://127.0.0.1:8000/')


# def techtool(request, home_id):
# return HttpResponse ("<h3> This page has all the tech tools </h3>")

def about(request):
    return render(request, 'about.html')


def donations(request):
    return render(request, 'donations.html')


def upload(request):
    if request.method == 'POST':
        uploads = FileUpload(request.POST, request.FILES)
        if uploads.is_valid():
            handle_uploaded_file(request.FILES['filepath'])
            model_instance = uploads.save(commit=False)
            model_instance.save()
            return HttpResponse("Worksheets Uploaded")
    else:
        uploads = FileUpload()
        return render(request, 'donations.html', {'form': uploads})


def worksheet(request):
    worksheetfiles = Worksheets.Object.all()
    return render(request, 'worksheets.html', {'worksheet': worksheetfiles})
