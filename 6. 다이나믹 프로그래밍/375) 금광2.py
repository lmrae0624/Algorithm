
for _ in range(int(input())):
    n,m=map(int,input().split())

    tmp=list(map(int,input().split()))
    graph=[]

    for i in range(n):
        graph.append(tmp[i*m:i*m+m])

    for i in range(1,m):
        for j in range(n):
            up,down=0,0
            if j-1>=0:
                up=graph[j-1][i-1]
            if j+1<n:
                down=graph[j+1][i-1]

            side=graph[j][i-1]

            graph[j][i]=max(up,down,side)+graph[j][i]

    max_value=0
    for i in range(n):
        max_value=max(max_value,graph[i][m-1])
    print(max_value)

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2