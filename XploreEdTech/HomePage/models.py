from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, User


# class User(AbstractUser):
#     pass

# class RegUser (models.Model):
#     username = models.CharField(max_length=50, null=True, unique=True)
#     email = models.CharField(max_length=50, null=True, unique=True)
#     password = models.CharField(max_length=100, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.email)

class Profile(models.Model):
    profileid = models.UUIDField(max_length=10, primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile', null=True)
    profession = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)
    # email = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    #
    # def __str__(self):
    #     return str(self.User)

    def __str__(self):
        return self.subjects



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
        return self.subject + ' ' + self.concept
