from django.shortcuts import render,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.
def index(request,):
    question_list= models.Question.objects.all()
    context={'question_list':question_list}
    return render(request,'polls/index.html',context)

def detail(request,pk):
    question= get_object_or_404(models.Question,pk=pk)
    return render(request,'polls/detail.html',{'question':question})


def result(request,pk):
    question= get_object_or_404(models.Question,pk=pk)
    return render(request,'polls/result.html',{'question':question})

def vote(request,pk):
    question= get_object_or_404(models.Question,pk=pk)
    return HttpResponseRedirect(reverse('polls:result',args=(question.id)))