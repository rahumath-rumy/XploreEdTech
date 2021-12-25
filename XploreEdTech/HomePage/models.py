from django.db import models
import uuid
from django.contrib.auth.models import User


class register_table(models.Model):
    profileid = models.UUIDField(max_length=10, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50, null=True, blank=True)
    grade_level = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    subjects = models.CharField(max_length=50, null=True, blank=True)
    # email = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.email


# class Subjects (models.Model):
#     subject = models.cCharField(max_length=50, null=True, unique=True)


class Worksheets(models.Model):
    worksheetID = models.UUIDField(max_length=10, primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=500)
    grade_level = models.CharField(max_length=500)
    concept = models.CharField(max_length=500)
    email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=50, null=True)
    filepath = models.FileField(upload_to="worksheets/", null=True)

    def __str__(self):
        return self.subject + '-' + self.concept

class TechTool(models.Model):
    toolID = models.UUIDField(max_length=10, primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=500)
    tool = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="edtechtool/", null=True)
    grade_level = models.CharField(max_length=500,  null=True)
    concept = models.CharField(max_length=500,  null=True)
    desc = models.CharField(max_length=1500,  null=True)
    link1 = models.CharField(max_length=1000, null=True)
    link2 = models.CharField(max_length=1000, null=True)
    link3 = models.CharField(max_length=1000, null=True)
    guide = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.subject + '-' + self.tool
