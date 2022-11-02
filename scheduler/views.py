from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    #emp1 
    employees_list = Employee.objects.all()
    for i in employees_list:
        print(i.skills)
    return render(request, 'home.html', {'emp1' : "sagar"})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    return render(request, "result.html", {'result': val1+val2})
