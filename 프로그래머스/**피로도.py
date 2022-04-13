def solution(k, dungeons):
    answer = 0
    
    from itertools import permutations 
    for i in range(len(dungeons)+1):
        for j in list(permutations(dungeons, i)):
            now=k
            count=0
            for need, spend in j:
                if now>=need:
                    count+=1 
                    now-=spend
            answer=max(answer,count)

    return answer

print(solution(80,[[10,20],[10,40],[30,10]]))


answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer