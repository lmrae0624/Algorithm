# 해당 칸으로 이동할수 있는 방법 수를 저장한다

def solution(m, n, puddles):
    answer = 0
    graph=[[0]*(m+1) for _ in range(n+1)] #편의성을 위해 +1을 해서 graph를 만들어줌

    for i in range(n+1):
        for j in range(m+1):
            if i==1 and j==1: #집이 있는 위치
                graph[i][j]=1
                continue

            if [j,i] in puddles: 
                graph[i][j]=0
            else:
                graph[i][j]=(graph[i-1][j]+graph[i][j-1])%1000000007 #오른쪽이랑 아래로만 이동할 수 있기 때문에
 
    return graph[n][m]

print(solution(4,3,[[2,2]]))