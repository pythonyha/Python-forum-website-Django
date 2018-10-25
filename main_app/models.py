from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    rezome=models.TextField(max_length=600)
    isactive= models.BooleanField(default=True)
    score= models.IntegerField(blank=True, null=True,default=0)
class category(models.Model):
    catname=models.CharField(max_length=100)
    update = models.DateTimeField(blank=True,auto_now_add=True)
    creative=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
class post(models.Model):
    owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    postTime=models.DateTimeField(auto_now=True)
    like= models.IntegerField(default=0,blank=True, null=True)
    isopen=models.BooleanField(default=True)
