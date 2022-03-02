from collections import defaultdict

id_list=list(map(str,input().split(',')))
report=list(map(str,input().split(',')))
k=int(input())

report=set(report)

a_list=defaultdict(set)
be_reported=defaultdict(int)
warning_list=[] 

answer=[0]*len(id_list)

for re in report:
    a, b=re.split()
    be_reported[b]+=1

    a_list[a].add(b)

    if be_reported[b]==k:
        warning_list.append(b)
    
warning_list=set(warning_list)

for w in warning_list:
    for i in range(len(id_list)):
        if w in a_list[id_list[i]]:
            answer[i]+=1
       
print(answer)


def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# muzi,frodo,apeach,neo
# muzi frodo,apeach frodo,frodo neo,muzi neo,apeach muzi 
# 2

# con,ryan
# ryan con,ryan con,ryan con,ryan con