from django.forms import ModelForm
from .models import Quiz

# Create the form class.
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'desc', 'time_in_sec', 'certificteImg']
