n=input()

dx=[1,-1,1,-1,2,2,-2,-2]
dy=[2,2,-2,-2,1,-1,1,-1]
x,y = ord(n[0]),int(n[1])

count=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx<ord('a') or nx>ord('h') or ny<1 or ny>8:
        continue
    
    count+=1
print(count)

    