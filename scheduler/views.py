from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from collections import defaultdict

# Create your views here.

def home(request):
    scheduleList = scheduleAlgorithm()
    return render(request, 'home.html', {'scheduleList' : scheduleList})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    return render(request, "result.html", {'result': val1+val2})

#Scheduling alogorithm

def scheduleAlgorithm():
    employees_list = Employee.objects.all() #input 1
    availability_list = Availability.objects.all() #input 2

    skills_map = defaultdict(list)
    availability_map = defaultdict(lambda:0)

    for i in range(len(employees_list)):
        skills_map[employees_list[i].id] = list(employees_list[i].skills.split(","))
        availability_map[employees_list[i].id] = availability_list[i].numberOfHours
    print(skills_map.items())
    print(availability_map.items())

    return main(employees_list, skills_map, availability_map)

def duplicate(testList, n):
    return [testList for _ in range(n)]
    
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def isGood(arr, skills_map):
    temp = []
    for i in arr:
        temp.extend(skills_map[i])
    if len(set(temp)) == 4:
        return True
    else:
        return False
        
def generate(nums, arr, i, N, ans, skills_map):
    if i == N:
        if isGood(arr, skills_map):
            ans.append(arr.copy())
        return
    else:
        arr.append(nums[i])
        generate(nums, arr, i+1, N, ans, skills_map)
        arr.pop(-1)
        generate(nums, arr, i+1, N, ans, skills_map)

def generate_subsets(skills_map):
    ans = []
    temp = sorted(skills_map, key=lambda k: len(skills_map[k]))
    print(temp)
    temp_skills = []
    temp_emp = []
    
    ans, arr = [], []
    i, N = 0, len(temp)
    generate(temp, arr, i, N, ans, skills_map)
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
    final_ans.sort()
    return(final_ans)

def main(employees_list, skills_map, availability_map):    
    adjusted_skills_map = defaultdict(list)
    for i in skills_map:
        j = availability_map[i]//4
        for k in range(1, j+1):
            new_key = str(i) + str(k)
            adjusted_skills_map[new_key] = skills_map[i]
    
    output_pairs = generate_subsets(adjusted_skills_map)
    for i in range(len(output_pairs)):
        val = ''
        for j in range(len(output_pairs[i])):
            val += Employee.objects.get(id=output_pairs[i][j][0]).name + " "
        output_pairs[i] = val
    
    #length of 10 since each slot is 4 hours long
    final_values = []
    for i in range(10):
        final_values.extend(duplicate(output_pairs[i],4))

    return to_matrix(final_values, 8)






#Test data

    # skills_map = defaultdict(list)
    # skills_map['1'] = [1,3]
    # skills_map['2'] = [2,4]
    # skills_map['3'] = [4,2]
    # skills_map['4'] = [3,1]
    # skills_map['5'] = [1,3,4]
    # skills_map['6'] = [2]
    # skills_map['7'] = [4,2,3]
    # skills_map['8'] = [1]

    
    # availability_map = defaultdict(lambda x:4)
    # availability_map['1'] = 12
    # availability_map['2'] = 12
    # availability_map['3'] = 12
    # availability_map['4'] = 8
    # availability_map['5'] = 12
    # availability_map['6'] = 8
    # availability_map['7'] = 8
    # availability_map['8'] = 12
        