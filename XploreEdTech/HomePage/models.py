from django.db import models

class RegUser (models.Model):
    username = models.CharField(max_length=50, null=True, unique=True)
    email = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)

# class Subjects (models.Model):
#     subject = models.cCharField(max_length=50, null=True, unique=True)
