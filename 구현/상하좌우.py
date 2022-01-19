n=int(input())
array=map(str,input().split())

x,y=1,1
# for a in array:
#     nx=x
#     ny=y
#     if a=='R':
#         ny=y+1
#     elif a=='L':
#         ny=y-1
#     elif a=='U':
#         nx=x-1
#     else:
#         nx=x+1
    
#     if nx<1 or nx>n or ny<1 or ny>n:
#         continue

#     x=nx
#     y=ny


dx=[0,0,-1,1]
dy=[1,-1,0,0]
move=['R','L','U','D']

for a in array:
    for i in range(4):
        if a==move[i]:
            nx=x+dx[i]
            ny=y+dy[i]
        
    if nx<1 or nx>n or ny<1 or ny>n:
        continue

    x,y = nx,ny

print(x,y)

# 5
# R R R U D D