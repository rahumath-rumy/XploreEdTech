from django import forms
from .models import *

class FileUpload(forms.ModelForm):
    class Meta:
        model = Worksheets
        fields = ["name", "school",  "email", "subject", "grade_level", "concept", "filepath"]