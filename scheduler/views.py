from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import *
from .scheduling_algorithm import *

#My view functions

def home(request):
    scheduleList = scheduleAlgorithm()
    return render(request, 'home.html', {'scheduleList' : scheduleList})

