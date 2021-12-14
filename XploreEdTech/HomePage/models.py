from django.db import models
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

class Profile (models.Model):
    profession = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.CharField(max_length=50, null=True, unique=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return str(self.User)


#class Subjects (models.Model):
#     subject = models.cCharField(max_length=50, null=True, unique=True)
