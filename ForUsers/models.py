from django.db import models
from django.contrib.auth.models import User
from ForCreators.models import Quiz, TempCertificte

class EndUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    Website = models.URLField( max_length=200, null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')


class Scores(models.Model):
    Quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    correctAnswer = models.CharField( max_length=5)
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)


class CertificteEraned(models.Model):
    certificte = models.ForeignKey(TempCertificte, on_delete=models.CASCADE)
    certificteImg = models.ImageField(upload_to='User Certificte' , max_length=None)
    isNFT= models.BooleanField(default=False)
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)

