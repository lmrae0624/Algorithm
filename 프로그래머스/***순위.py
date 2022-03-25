def solution(n, results):
    answer = 0
    graph=[[0]*n for _ in range(n)]

    for r in results:
        graph[r[0]-1][r[1]-1]=1 #이긴 경우
        graph[r[1]-1][r[0]-1]=-1 #진 경우

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]!=0: #이기거나 진거가 이미 판단가능해서 0이아니면 continue
                    continue
                
                if graph[i][k] == graph[k][j] :
                    graph[i][j] = graph[i][k]
                    graph[j][i] = -graph[i][k]

    for i in range(n):
        if 0 in graph[i][:i] + graph[i][i+1:]: #graph[i][i]를 제외하고 0이있으면 continue
            continue
        answer += 1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))