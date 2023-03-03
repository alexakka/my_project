from django.shortcuts import render, HttpResponse
from .models import Survey, Question, Choice


# Create your views here.
def index(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/index.html', context={'surveys': surveys})


def detail(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    return render(request, 'surveys/detail.html', context={'survey': survey})


