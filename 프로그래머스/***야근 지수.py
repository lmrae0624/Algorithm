def solution(n, works):
    import heapq
    answer = 0

    if sum(works)<=n:
        return 0
    
    h=[]
    for i in works:
        heapq.heappush(h,-i)

    for i in range(n):
        heapq.heappush(h,heapq.heappop(h)+1)

    return sum([i*i for i in h])

print(solution(4,[4, 3, 3]))

print(solution(1,[2, 1, 2]))