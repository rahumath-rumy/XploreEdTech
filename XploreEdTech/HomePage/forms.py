from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# class RegUser(ModelForm):
#     class Meta:
#         model = RegUser
#         fields = "__all__"

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         # fields = ["profession", "grade_level",  "school", "subjects"]
#         fields = ['subjects', 'profession']

class FileUpload(forms.ModelForm):
    class Meta:
        model = Worksheets
        fields = ["name", "school",  "email", "subject", "grade_level", "concept", "filepath"]