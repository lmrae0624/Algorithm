import heapq

def solution(food_times, k):
    answer = 0

    if sum(food_times)<=k:
        return -1

    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    prev_value=0
    sum_time=0
    length=len(food_times)

    while True:
        min_value, i=heapq.heappop(q)
        
        now_value=(min_value-prev_value)*length

        if sum_time+now_value > k:
            heapq.heappush(q,(min_value,i))
            break

        sum_time+=now_value
        length-=1
        prev_value=min_value

    answer=sorted(q, key=lambda x:x[1])

    return answer[(k-sum_time)%length][1] # 마지막 index 음식을 먹었을 때 첫번째거 출력해야되니까 %length 해주기


food_times=list(map(int,input().split()))
k=int(input())
print(solution(food_times, k))

# 3 1 2
# 5

# 2 2 2
# 3

