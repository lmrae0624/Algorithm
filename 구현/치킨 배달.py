n,m=map(int,input().split())

house=[]
chicken=[]
for i in range(n):
    tmp=list(map(int,input().split()))  
    for j in range(n):
        if tmp[j]==1:
            house.append((i,j))
        elif tmp[j]==2:
            chicken.append((i,j))
    
# def distance():
#     country_dist=0
#     for h in house:
#         min_dist=1e9
#         for c in chicken:
#             min_dist=min(min_dist,(abs(h[0]-c[0])+abs(h[1]-c[1])))
#         country_dist+=min_dist
#     return country_dist
    
# result=1e9
# def solution():
#     global result

#     if len(chicken)==m:
#         result=min(result,distance())
#         return result
#     else:
#         for i in range(len(chicken)):
#             x,y=chicken.pop(0)
#             solution()
#             chicken.append((x,y))
#     return result

from itertools import combinations #조합
candidates = list(combinations(chicken, m))

def distance(candidate):
    country_dist=0

    for h in house:
        min_dist=1e9
        for c in candidate:
            min_dist=min(min_dist,(abs(h[0]-c[0])+abs(h[1]-c[1])))
        country_dist+=min_dist
    return country_dist

result=1e9
for candidate in candidates:
    result=min(result,distance(candidate))

print(result)

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1


