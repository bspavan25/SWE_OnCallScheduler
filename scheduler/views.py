from django.http import HttpResponse
from django.shortcuts import render
from .models import *

#Scheduling alogorithm

def scheduleAlgorithm():
    employees_list = Employee.objects.all() #input 1
    availability_list = Availability.objects.all() #input 2
    
    scheduleList = [['default']*8]*5 #final schedule

    for i in range(len(employees_list)):
        print(employees_list[i].id, employees_list[i].skills, end = " ")
        print(availability_list[i].numberOfHours)
    return scheduleList

# Create your views here.

def home(request):
    scheduleList = scheduleAlgorithm()
    return render(request, 'home.html', {'scheduleList' : scheduleList})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    return render(request, "result.html", {'result': val1+val2})



