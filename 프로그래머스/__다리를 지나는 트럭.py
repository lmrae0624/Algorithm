def solution(bridge_length, weight, truck_weights):
    answer = 0

    time=[0]*len(truck_weights)
    num=len(truck_weights)
    move={}
    total=0
    depart=[]
    while True:
        answer+=1
        if total<=weight:
            tmp=truck_weights.pop(0)
            total+=tmp
            move[tmp].append(1)
        
        for m in move:
            m

        
        if len(depart)==num:
            break

    return answer


print(solution(2,10,[7,4,5,6]))