from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20,default="")
    last_name=models.CharField(max_length=20,default="")
    city = models.CharField(max_length=20,default="")
    country=models.CharField(max_length=20,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    rezome=models.TextField(max_length=600)
    isactive= models.BooleanField(default=True)
    score= models.IntegerField(blank=True, null=True,default=0)
    pic = models.ImageField(blank=True , upload_to='users/image/')

    def save(self):
        im = Image.open(self.pic)
        output = BytesIO()
        im = im.resize( (250,270) )
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.pic = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.pic.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(profile_pic,self).save()






class category(models.Model):
    catname=models.CharField(max_length=100)
    update = models.DateTimeField(blank=True,auto_now_add=True)
    creative=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
class post(models.Model):
    owner=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    postTime=models.DateTimeField(auto_now=True)
    like= models.IntegerField(default=0,blank=True, null=True)
    isopen=models.BooleanField(default=True)
