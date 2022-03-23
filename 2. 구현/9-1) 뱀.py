n=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]

k=int(input())
for _ in range(k):
    x, y = map(int,input().split())
    graph[x][y]=1
    
l=int(input())
move=[]
for _ in range(l):
    sec, d=map(str,input().split())
    move.append((int(sec),d))


dx = [0, 1, 0, -1] #동 남 서 북
dy = [1, 0, -1, 0]


def turn(direction, t):
    if t=='L':
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction


def solution():
    x, y= 1,1
    graph[x][y]=2
    direction=0 #뱀이 바라보고 있는 방향
    time=0

    q=[(x,y)]

    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny]==0:
                px,py=q.pop(0)
                graph[px][py]=0

            graph[nx][ny]=2
            q.append((nx,ny))
            x,y=nx,ny
        else:
            time+=1
            break

        time+=1
        if len(move)>0 and time == move[0][0]:
            direction=turn(direction,move[0][1])
            move.pop(0)

    return time

print(solution())
        
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L