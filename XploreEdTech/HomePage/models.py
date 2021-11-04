from django.db import models

# Create your models here.
class allusers(models.Model):
    username=models.CharField(max_length=14)
    firstname=models.CharField(max_length=100)
    def __str__(self):
        return self.username

class details(models.Model):
    subjects=models.ForeignKey(allusers, on_delete=models.CASCADE)
    school=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    def __str__(self):
        return self.role
