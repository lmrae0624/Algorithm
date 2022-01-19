import heapq
from xxlimited import foo
food_times=list(map(int,input().split()))
k=int(input())

if sum(food_times)<=k:
    print(-1)
else:
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))


# 3 1 2
# 5