from collections import defaultdict
from .models import *

#Scheduling alogorithm

def scheduleAlgorithm():
    employees_list = Employee.objects.all() #input 1
    availability_list = Availability.objects.all() #input 2

    skills_map = defaultdict(list)
    availability_map = defaultdict(lambda:0)

    for i in range(len(employees_list)):
        skills_map[employees_list[i].id] = list(employees_list[i].skills.split(","))
        availability_map[employees_list[i].id] = availability_list[i].numberOfHours

    #print(skills_map.items())
    #print(availability_map.items())

    return scheduleAlgorithmHelper(employees_list, skills_map, availability_map)

#Helper functions

def scheduleAlgorithmHelper(employees_list, skills_map, availability_map):    
    adjusted_skills_map = defaultdict(list)
    for i in skills_map:
        j = availability_map[i]//4
        for k in range(1, j+1):
            new_key = str(i) + str(k)
            adjusted_skills_map[new_key] = skills_map[i]
    
    output_pairs, buffer_pairs = generate_subsets(adjusted_skills_map)
    #print()
    #print(buffer_pairs)
    #print(len(buffer_pairs))

    for i in range(len(output_pairs)):
        val = ''
        for j in range(len(output_pairs[i])):
            val += Employee.objects.get(id=output_pairs[i][j][0]).name + " "
        output_pairs[i] = val

    for i in range(len(buffer_pairs)):
        val = ''
        for j in range(len(buffer_pairs[i])):
            val += Employee.objects.get(id=buffer_pairs[i][j][0]).name + " " + "*"
        buffer_pairs[i] = val
    
    #length of 10 since each slot is 4 hours long
    final_values = []
    for i in range(len(output_pairs)):
        final_values.extend(duplicate(output_pairs[i],4))

    for i in range(len(buffer_pairs)):
        final_values.extend(duplicate(buffer_pairs[i],4))
    
    for i in range(40):
        final_values.append("N/A N/A ")

    return to_matrix(final_values[:40], 8)

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
        
def generate(nums, arr, i, N, ans, skills_map, buffer_pairs):
    if i == N:
        if isGood(arr, skills_map):
            ans.append(arr.copy())
        else:
            buffer_pairs.append(arr.copy())
        return
    else:
        arr.append(nums[i])
        generate(nums, arr, i+1, N, ans, skills_map, buffer_pairs)
        arr.pop(-1)
        generate(nums, arr, i+1, N, ans, skills_map, buffer_pairs)

def generate_subsets(skills_map):
    ans = []
    temp = sorted(skills_map, key=lambda k: len(skills_map[k]))
    print(temp)
    temp_skills = []
    temp_emp = []
    
    ans, arr = [], []
    buffer_pairs = []
    i, N = 0, len(temp)
    generate(temp, arr, i, N, ans, skills_map, buffer_pairs)
    #print(ans)
    ans.sort(key=lambda k: len(k))
    buffer_pairs.sort(key=lambda k: len(k))
    final_ans = []
    final_buffers = []
    visited = set()
    #buffer_visited = set()
    
    for i in range(len(ans)):
        check = True
        for j in ans[i]:
            if j in visited:
                check = False
                break
        if check:
            final_ans.append(ans[i])
            for j in ans[i]:
                visited.add(j)

    final_ans.sort()

    print("final ans")
    print(final_ans)
    print(visited)

    for i in range(len(buffer_pairs)):
        check = True
        for j in buffer_pairs[i]:
            if j in visited:
                check = False
                break
        if check and len(buffer_pairs[i])>0:
            final_buffers.append(buffer_pairs[i])
            for j in buffer_pairs[i]:
                visited.add(j)

    return final_ans, final_buffers[:40]

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
        