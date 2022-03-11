
def solution(bridge_length, weight, truck_weights):
    answer = 0

    total=0
    move_truck=[]
    move_time=[]
    while truck_weights:
        answer+=1
        if total+truck_weights[0]<=weight:
            tmp=truck_weights.pop(0)
            total+=tmp
            move_truck.append(tmp)
            move_time.append(0)
       
        for i in range(len(move_time)):
            move_time[i]+=1

        if move_time[0]>=bridge_length:
            move_time.pop(0)
            total-=move_truck.pop(0)

    return answer+bridge_length

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))