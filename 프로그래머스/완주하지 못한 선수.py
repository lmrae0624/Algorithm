participant=list(map(str,input().split(',')))
completion=list(map(str,input().split(',')))

answer=''
participant.sort()
completion.sort()
for i in range(len(participant)):
    if participant[i]!=completion[i]:
        answer=participant[i]
        break

print(answer)

# leo,kiki,eden
# eden,kiki

# mislav,stanko,mislav,ana
# stanko,ana,mislav


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    print(collections.Counter(participant) ) #Counter({'mislav': 2, 'ana': 1, 'stanko': 1})
    print(collections.Counter(completion)) #Counter({'ana': 1, 'mislav': 1, 'stanko': 1})
    
    return list(answer.keys())[0]

solution(participant,completion)