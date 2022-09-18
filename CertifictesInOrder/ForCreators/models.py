from email.policy import default
from django.db import models
from users.models import Profile
# Create your models here.



class Quiz(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)    
    time_in_sec = models.IntegerField(help_text="Duration of the quiz in seconds", default="1")
    certificteImg = models.ImageField(upload_to='TemplateCertificte' , max_length=None,default="DefaultTemplateCertificte.png")
    
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



