def solution(progresses, speeds):
    answer = []

    count=0
    while len(progresses)>0:
        for i in range(len(progresses)):
            if progresses[i]<100:
                progresses[i]+=speeds[i]

        while True:
            if len(progresses)==0:
                break
            if progresses[0]>=100:
                count+=1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        
        if count!=0:
            answer.append(count)
            count=0

    return answer

print(solution([93, 30, 55],[1, 30, 5]))

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
    

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

