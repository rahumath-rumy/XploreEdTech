import os.path

import stripe as stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import FileUpload, UserCreationForm
from django.contrib import messages
from .models import *
from .models import Worksheets
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file
from django.contrib.auth.models import User
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    common_tool = TechTool.objects.all().filter(subject="Suitable for any subject")
    return render(request, "index.html", {'common_tool': common_tool})


def register(request):
    if request.method == "POST":
        # fname = request.POST['firstname']
        un = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['confirmpwd']
        school = request.POST['school']
        sub = request.POST['subject']
        gl = request.POST['gl']
        role = request.POST['prof']

        if pwd == cpwd:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=un).exists():
                messages.info(request, "The Email or Username already exists ")
            # print("Email or Username already exists ")
            # if User.objects.filter(username=un).exists():
            #     print("Username already exists")
            else:
                usr = User.objects.create_user(un, email, pwd)
                usr.save()

                reg = register_table(user=usr, subjects=sub, grade_level=gl, profession=role, school=school)
                reg.save()
                return render(request, "profile.html",
                              {"status": "{} , Welcome! Your Account has been created successfully!".format(un)})
                # return render(request, 'profile.html')
        else:
            messages.info(request, "The Passwords Do Not Match! ")
            # print("Passwords dont match")
    return render(request, "signup.html")


# def signup(request):
#     #main one
#     #form = CreateUserForm()
#     if request.method == 'POST':
#         form = ExtendedUserCreationForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#
#         if form.is_valid() and profile_form.is_valid():
#             user = form.save()
#
#             profile_f = profile_form.save(commit=False)
#             profile_f.user = user
#             profile_f.save()
#
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Welcome ' + user + ' your account has been created!')
#             return redirect('getstarted.html')
#     else:
#         form = ExtendedUserCreationForm()
#         profile_form = ProfileForm()
#     # form = User.objects.all()
#     context = {'form': form, 'profile_form': profile_form}
#     return render(request, 'signup.html', context)
#
# #till here
#
#


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


def checkout(request):
    return render(request, 'checkout.html')


@login_required(login_url='login')
def profile(request):
    context = {}
    prof = register_table.objects.get(user__id=request.user.id)
    context["prof"] = prof
    if request.method == "POST":
        # un = request.POST['username']
        # email = request.POST['email']
        school = request.POST['school']
        sub = request.POST['subject']
        gl = request.POST['gl']
        role = request.POST['prof']

        usr = User.objects.get(id=request.user.id)
        # usr.email = email
        usr.save()

        prof.school = school
        prof.subjects = sub
        prof.grade_level = gl
        prof.profession = role
        prof.save()
        # context["status"] = "Updated Profile"
        return render(request, "profile.html", {"status": "{} Your Profile Has Been Updated"})

    return render(request, "profile.html", context)


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
        return render(request, 'upload.html', {'form': uploads})
    # return render(request, 'upload.html')


def worksheet(request):
    worksheet_files = Worksheets.objects.all()
    return render(request, 'worksheets.html', {'worksheet_files': worksheet_files})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),
                                    content_type="static/worksheet")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
        raise Http404


def wksearch(request):
    # if request.method  == 'GET':
    wksearch = request.GET['wksearch']
    # wksearch1 = request.GET['wksearch1']
    data = Worksheets.objects.filter(subject__icontains=wksearch).order_by('-worksheetID')
    # data1 = Worksheets.objects.filter(concept__icontains=wksearch1).order_by('-worksheetID')
    # dataaa = data and data1
    return render(request, 'search.html', {"data": data})

def wksearch1(request):
    wksearch1 = request.GET['wksearch1']
    data = TechTool.objects.filter(subject__icontains=wksearch1).order_by('-worksheetID')
    return render(request, 'search.html', {"data": data})

# User = User.objects.all().extra(tables=['animal'],
#                                 where=[
#                                     'user.name = animal.name',
#                                     'user.age > 18'
#                                 ]
#                                 )
def commontools(request):
    common_tool = TechTool.objects.all().filter(subject="Suitable for any subject")
    return render(request, "commonedtech.html", {'common_tool': common_tool})


def mathtool(request):
    common_tool = TechTool.objects.all().filter(subject__contains="Math")
    return render(request, "commonedtech.html", {'common_tool': common_tool})

def langtool(request):
    common_tool = TechTool.objects.all().filter(subject__icontains="Lang")
    return render(request, "language.html", {'common_tool': common_tool})

class payment(TemplateView):
    template_name = 'payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='LKR',
            description="test",
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')