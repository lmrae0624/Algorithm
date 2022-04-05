def solution(maps):
    from collections import deque
    answer = 0
    n=len(maps) #행
    m=len(maps[0]) #열

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    q=deque([(0,0)])

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m or maps[nx][ny]>1:
                continue

            if maps[nx][ny]==1:
                q.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1
    
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))