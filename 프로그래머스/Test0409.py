def solution(path):
    answer=[]

    def direc_check(now,next):
        if now=='E':
            if next=='N':
                return 'left'
            else:
                return 'right'
        elif now=='W':
            if next=='S':
                return 'left'
            else:
                return 'right'
        elif now=='N':
            if next=='W':
                return 'left'
            else:
                return 'right'
        else:
            if next=='E':
                return 'left'
            else:
                return 'right'

    now=path[0]
    time=0
    count=1

    for i in range(1,len(path)):
        time+=1
        if now==path[i]:
            count+=1
        else:
            if count>5:
                count=5
            answer.append("Time "+str(time-count)+": Go straight "+str(count)+"00m and turn "+direc_check(now,path[i]))     
            count=1
            now=path[i]

    return answer

#print(solution("EEESEEEEEENNNN"))
print(solution("SSSSSSWWWNNNNNNWWWN"))
print(solution("SSSSSSN"))