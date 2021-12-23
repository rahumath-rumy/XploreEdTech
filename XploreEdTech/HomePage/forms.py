from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
            return user

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