
def solution(N, road, K):
    import heapq
    
    distance=[1e9]*(N+1)
    graph=[[]*(N+1) for i in range(N+1)]
    for x,y,dist in road:
        graph[x].append((y,dist))
        graph[y].append((x,dist))
    
    h=[]
    start, cost= 1,0
    heapq.heappush(h,(cost,start))
    distance[start]=cost

    while h:
        cost,now=heapq.heappop(h)
        
        if cost>distance[now]:
            continue

        for next, dist in graph[now]:
            total=cost+dist
            if distance[next]>total:
                distance[next]=total
                heapq.heappush(h,(total,next))
    answer=0
    for a in distance:
        if a<=K:
            answer+=1

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))