INF=int(1e9)
n, m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

result=0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1,n+1):
    count=0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print('I',end=' ')
        else: 
            print(graph[i][j],end=' ')
    print()

# 입력 예시
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4