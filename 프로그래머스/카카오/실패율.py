def solution(N, stages):
    stages.sort()
    
    result={}
    pnum=len(stages)

    for i in range(1,N+1):
        if stages.count(i)==0:
            result[i]=0
        else:
            result[i]=stages.count(i)/pnum
        pnum-=stages.count(i)
    print(result)
    answer = sorted(result, key=result.get,reverse = True)

    #return sorted(result, key=lambda x : result[x], reverse=True)
    return answer



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
 #result=sorted(result.items(), key = lambda x: x[1], reverse = True)