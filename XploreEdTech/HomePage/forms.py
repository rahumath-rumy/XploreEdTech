from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import Worksheets, Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserEditProfile (UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class RegUser(ModelForm):
#     class Meta:
#         model = RegUser
#         fields = "__all__"

class Profile(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ["profession", "grade_level",  "school", "subjects"]
        fields = ["subjects"]

class FileUpload(forms.ModelForm):
    class Meta:
        model = Worksheets
        fields = ["name", "school",  "email", "subject", "grade_level", "concept", "filepath"]