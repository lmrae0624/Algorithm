import heapq

INF=int(1e9)
t=int(input())
move=[(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(t):
    n=int(input())
    graph=[[INF]*(n) for i in range(n)]
    
    energy=[]
    for i in range(n):
        energy.append(list(map(int,input().split())))

    q=[]
    graph[0][0]=energy[0][0]
    q = [(energy[0][0], 0, 0)]  #heapq.heappush(q,(energy[0][0],0,0))

    while q:
        value, x, y =heapq.heappop(q)

        if graph[x][y] < value:
              continue

        for m in move:
            nx=x+m[0]
            ny=y+m[1]

            # or로 효율 높이기
            # if nx < 0 or nx >= n or ny < 0 or ny >= n:
            #       continue

            if 0<=nx and nx<n and 0<=ny and ny<n:
                cost=value+energy[nx][ny]
                if cost < graph[nx][ny]:
                    graph[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny)) 

    print(graph[n-1][n-1])

    for i in range(n):
        for j in range(n):
            print(graph[i][j],end=' ')
        print()

#입력 예시
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
