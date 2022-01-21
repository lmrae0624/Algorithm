n=int(input())
power=list(map(int,input().split()))
d=[1]*n

power.reverse()

for i in range(1,n):
    for j in range(0,i):
        if power[i] > power[j]:
            d[i]=max(d[i],d[j]+1)

print(n-max(d))


# from bisect import bisect_left as bl
# def LIS(L):
#     best = []
#     for i in L:
#         pos = bl(best, i) #pos=best에 i가 들어갈 위치
#         if len(best) <= pos: best.append(i) 
#         else: best[pos] = i #현재 best[pos]값보다 i 값이 더 작기 때문에 차이를 줄여주기 위해 변경
#     return len(best)

# n = int(input())
# A = list(map(int,input().split()))[::-1]
# print(n - LIS(A))