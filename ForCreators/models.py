from ast import ClassDef
from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User


class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    youtube= models.URLField( max_length=200)
    website= models.URLField( max_length=200)


    def __str__(self):
        return self.user.username

