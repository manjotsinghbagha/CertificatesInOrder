from re import S
from django.shortcuts import render,redirect
from .models import QuesModel, Quiz
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from .forms import QuizForm
# Create your views here.


class QuizListView(ListView):
    model = Quiz
    template_name = "list.html"

def addQuiz(request):
    if request.POST :
        form = QuizForm(request.POST or None, request.FILES or None)
        # form.maker_id = request.user
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect('add/'+ form.name +'/',request)
        return render(request, "create.html", {'form':form})
    else:
        form = QuizForm()
        return render(request, "create.html", {'form':form})
    
@login_required
def index(request, quiz_id):
    quiz = Quiz.objects.get(name=quiz_id)
    if quiz.maker.user == request.user:
        # quesFormset = modelformset_factory(QuesModel, fields=('question','op1','op2','op3','op4','ans'))
        quesFormset = inlineformset_factory(Quiz,QuesModel,fields=('question','op1','op2','op3','op4','ans'),extra=1,)
        if request.method == "POST":
            # formset = quesFormset(request.POST,queryset=QuesModel.objects.filter(quiz_id=quiz_id))
            formset = quesFormset(request.POST,instance=quiz)
            if  formset.is_valid():
                formset.save()
                # instances = formset.save(commit=False)
                # for instance in instances :
                    # instance.quiz_id = quiz.id
                    # instance.save()
                return redirect('index', quiz_id = quiz.name)
        # formset = quesFormset(queryset=QuesModel.objects.filter(quiz_id=quiz_id))
        formset = quesFormset(instance=quiz)
        return render(request, 'index.html',{'formset':formset})
    else:
        return redirect("/",request)


@login_required
def test(request,quiz_name ):
    if request.method=='POST':
        pass
    else:
        quiz = Quiz.objects.get(name=quiz_name)
        ques = QuesModel.objects.get(quiz=quiz_name)
        return render(request,'test.html',{'quiz':quiz,'ques':ques})
    

