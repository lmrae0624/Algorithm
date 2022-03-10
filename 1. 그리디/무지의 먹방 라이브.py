import heapq

food_times=list(map(int,input().split()))
k=int(input())

if sum(food_times)<=k:
    print(-1)
else:
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    previous=0
    sum_time=0
    length=len(food_times)

    while True:
        min_value,index=heapq.heappop(q)
        now=(min_value-previous)*length
        if sum_time+now > k:
            heapq.heappush(q,(min_value,index))
            break
        sum_time+=now
        length-=1
        previous=min_value

    # while sum_value + ((q[0][0] - previous) * length) <= k:
    #     now = heapq.heappop(q)[0]
    #     sum_value += (now - previous) * length
    #     length -= 1 # 다 먹은 음식 제외
    #     previous = now # 이전 음식 시간 재설정
    
    result=sorted(q,key=lambda x:x[1])
    print(q)
    print(result[k-sum_time][1])  #틀림 
        
# 3 1 2
# 5