from django.db import models
import os, random, string
from django.contrib.auth.models import User

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'UserCert'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class Quiz(models.Model):
    # maker = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True,primary_key=True)
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

class Scores(models.Model):
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correctAnswer = models.CharField( max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Quiz_SN = models.SlugField(unique=True, editable=False)
    def save(self, *args, **kwargs):
        while not self.Quiz_ID:
            newslug = ''.join([
                random.sample(string.letters, 2),
                random.sample(string.digits, 2),
                random.sample(string.letters, 2),
            ])

            if not self.objects.filter(pk=newslug).exists():
                self.Quiz_ID = newslug

        super().save(*args, **kwargs)



class Certificte(models.Model):
    certificte = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    certificteID = models.SlugField(primary_key=True, unique=True, editable=False)
    isNFT= models.BooleanField(default=False)
    enduser = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        while not self.certificteID:
            newslug = ''.join([
                random.sample(string.letters, 2),
                random.sample(string.digits, 2),
                random.sample(string.letters, 2),
            ])

            if not self.objects.filter(pk=newslug).exists():
                self.certificteID = newslug

        super().save(*args, **kwargs)

    class Meta:
        abstract = True