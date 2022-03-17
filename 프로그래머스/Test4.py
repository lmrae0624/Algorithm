def solution(data):
    answer=[]
    wait=[]

    while data or wait: #data나 wait가 둘다 비어있으면 끝
        if wait: # wait에 값이 들어있을 때 
            wait.sort()
            page,index=wait.pop(0)
            time+=page
        else: 
            index,t,page=data.pop(0)
            time=t+page
        
        answer.append(index)

        while data and time>=data[0][1]:
            index,t,page=data.pop(0)
            wait.append([page,index])

    return answer


print(solution([[1,0,5],[2,2,2],[3,3,1],[4,4,1],[5,10,2]])) #13425
print(solution([[1,0,3],[2,1,3],[3,3,2],[4,9,1],[5,10,2]])) #13245
print(solution([[1,2,10],[2,5,8],[3,6,9],[4,20,6],[5,25,5]])) #12452
