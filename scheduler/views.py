from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from collections import defaultdict

#Scheduling alogorithm

def scheduleAlgorithm():
    employees_list = Employee.objects.all() #input 1
    availability_list = Availability.objects.all() #input 2

    skills_map = defaultdict(list)
    availability_map = defaultdict(lambda:0)

    #final output
    scheduleList = [['Sagar, srikanth, pavan']*8]*5 #final schedule

    for i in range(len(employees_list)):
        skills_map[employees_list[i].id] = list(employees_list[i].skills.split(","))
        availability_map[availability_list[i].id] = availability_list[i].numberOfHours
    print(skills_map.items())
    print(availability_map.items())

    return scheduleList

# Create your views here.

def home(request):
    scheduleList = scheduleAlgorithm()
    return render(request, 'home.html', {'scheduleList' : scheduleList})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    return render(request, "result.html", {'result': val1+val2})




#core Algorithm

def isGood(arr):
    temp = []
    for i in arr:
        temp.extend(skills_map[i])
    if len(set(temp)) == 4:
        return True
    else:
        return False
        
def generate(nums, arr, i, N, ans):
    if i == N:
        if isGood(arr):
            ans.append(arr.copy())
        return
    else:
        arr.append(nums[i])
        generate(nums, arr, i+1, N, ans)
        arr.pop(-1)
        generate(nums, arr, i+1, N, ans)

def generate_subsets(skills_map):
    ans = []
    temp = sorted(skills_map, key=lambda k: len(skills_map[k]))
    print(temp)
    temp_skills = []
    temp_emp = []
    
    ans, arr = [], []
    i, N = 0, len(temp)
    generate(temp, arr, i, N, ans)
    #print(ans)
    ans.sort(key=lambda k: len(k))
    final_ans=[]
    visited = set()
    prev = None
    
    for i in range(len(ans)):
        check = True
        for j in ans[i]:
            if j in visited:
                check = False
                continue
        if check:
            final_ans.append(ans[i])
            for j in ans[i]:
                visited.add(j)
    return(final_ans)



skills_map = defaultdict(list)
skills_map['a'] = [1,3]
skills_map['b'] = [2,3]
skills_map['c'] = [2,4]
skills_map['d'] = [1,4]
skills_map['e'] = [1,3,4]
skills_map['f'] = [2]

print(generate_subsets(skills_map))

