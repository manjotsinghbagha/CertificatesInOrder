from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Creator(models.Model):
    isVerified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    youtube = models.URLField( max_length=200)
    Website = models.URLField( max_length=200)

    def __str__(self):
        return self.user.username

class TempCertificte(models.Model):
    certificteImg = models.ImageField(upload_to='TemplateCertificte' , max_length=None,default="DefaultTemplateCertificte.png")
    CertificteName = models.CharField( max_length=50)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)

class Quiz(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    
    def __str__(self):
        return self.name

class QuesModel(models.Model):
    quiz = models.ForeignKey(Quiz,  on_delete=models.CASCADE)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question



