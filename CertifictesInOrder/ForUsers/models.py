from django.db import models
from users.models import Profile
from ForCreators.models import Quiz
import string, random
from django.db import models
import os


class Scores(models.Model):
    Quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    correctAnswer = models.CharField( max_length=5)
    enduser = models.ForeignKey(Profile, on_delete=models.CASCADE)


def path_and_rename(instance, filename):
    upload_to = 'UserCert'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)
    
class CertificteEraned(models.Model):
    certificte = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    certificteID = models.SlugField(primary_key=True, unique=True, editable=False, blank=True)
    isNFT= models.BooleanField(default=False)
    enduser = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        while not self.slug:
            newslug = ''.join([
                random.sample(string.letters, 2),
                random.sample(string.digits, 2),
                random.sample(string.letters, 2),
            ])

            if not self.objects.filter(pk=newslug).exists():
                self.slug = newslug

        super().save(*args, **kwargs)

    class Meta:
        abstract = True



