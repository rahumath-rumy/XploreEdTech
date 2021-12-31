import os.path

import stripe as stripe
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import FileUpload
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
    common_tool = TechTool.objects.all().filter(subject="Suitable for any subject")[:4]
    return render(request, "index.html", {'common_tool': common_tool})


def register(request):
    if request.method == "POST":
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
            else:
                usr = User.objects.create_user(un, email, pwd)
                usr.save()

                reg = register_table(user=usr, subjects=sub, grade_level=gl, profession=role, school=school)
                reg.save()
                return render(request, "profile.html",
                              {"status": "{} , Welcome! Your Account has been created successfully!".format(un)})
        else:
            messages.info(request, "The Passwords Do Not Match! ")
    return render(request, "signup.html")

@login_required(login_url='login')
def profile(request):
    context = {}
    prof = register_table.objects.get(user__id=request.user.id)
    context["prof"] = prof
    if request.method == "POST":
        school = request.POST['school']
        sub = request.POST['subject']
        gl = request.POST['gl']
        role = request.POST['prof']

        usr = User.objects.get(id=request.user.id)
        usr.save()

        prof.school = school
        prof.subjects = sub
        prof.grade_level = gl
        prof.profession = role
        prof.save()
        return render(request, "index.html", {"status": "{} Your Profile Has Been Updated"})

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
    wksearch = request.GET['wksearch']
    data = Worksheets.objects.filter(subject__icontains=wksearch).order_by('-worksheetID')
    return render(request, 'search.html', {"data": data})

def toolsearch(request):
    toolsearch = request.GET['toolsearch']
    data1 = TechTool.objects.filter(concept__icontains=toolsearch).order_by('-toolID')
    return render(request, 'EdTechCat/searchtool.html', {"data1": data1})

def ctoolsearch(request):
    ctoolsearch = request.GET['ctoolsearch']
    data2 = TechTool.objects.filter(tool__icontains=ctoolsearch).order_by('-toolID')
    return render(request, 'EdTechCat/csearchtool.html', {"data2": data2})

def commontools(request):
    common_tool = TechTool.objects.all().filter(subject="Suitable for any subject")
    return render(request, "EdTechCat/commonedtech.html", {'common_tool': common_tool})

def mathtool(request):
    common_tool = TechTool.objects.all().filter(subject__contains="Math")
    return render(request, "EdTechCat/maths.html", {'common_tool': common_tool})

def langtool(request):
    common_tool = TechTool.objects.all().filter(subject__icontains="Lang")
    return render(request, "EdTechCat/language.html", {'common_tool': common_tool})

def sciencetool(request):
    common_tool = TechTool.objects.all().filter(subject__icontains="Sci")
    return render(request, "EdTechCat/science.html", {'common_tool': common_tool})

def preschooltool(request):
    common_tool = TechTool.objects.all().filter(subject__icontains="Pre")
    return render(request, "EdTechCat/preschool.html", {'common_tool': common_tool})

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