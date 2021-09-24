from django.db import models

# Create your models here.
class login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    u_type = models.CharField(max_length=25)


class faculty(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=25)
    age = models.IntegerField()
    subject = models.CharField(max_length=25)
    department=models.CharField(max_length=25)
    email=models.CharField(max_length=40)

class student(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=25)
    s_class = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.CharField(max_length=40)
