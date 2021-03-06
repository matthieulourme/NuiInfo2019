"""moulinette URL Configuration

The `urlpatterns` list routes URL

from django.http import HttpResponse"""
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from asterios.models import Question,Choice


def index(request):
    '''latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}'''
    return render(request, 'asterios/index.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'asterios/detail.html', {'question': question})

def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'asterios/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'asterios/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def test(request):
    return render(request,'asterios/test.html')

def aide_sociale(request):
    return render(request,'asterios/aide_sociale.html')

def aides(request):
    return render(request,'asterios/aides.html')

def baisse_apl(request):
    return render(request,'asterios/baisse_apl.html')

def conditions_vie(request):
    return render(request,'asterios/conditions_vie.html')

def difficultes(request):
    return render(request,'asterios/difficultes.html')

def precarite(request):
    return render(request,'asterios/precarite.html')


def page_not_found_view(request):
    return render(request, 'asterios/404.html')
