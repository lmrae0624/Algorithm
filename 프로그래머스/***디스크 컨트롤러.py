
def solution(jobs):
    import heapq
    n=len(jobs)
    current_time=0 # 현재시간
    total_time=0 # 총 시간
    
    jobs.sort()
    
    h=[]
    while h or jobs:
        while jobs and jobs[0][0]<=current_time:
            start,t=jobs.pop(0)
            heapq.heappush(h,[t,start])
        
        if not h:
            start,t=jobs.pop(0)
            heapq.heappush(h,[t,start])
            
        t,start=heapq.heappop(h)

        if start<=current_time:
            current_time+=t
        else:
            current_time=start+t
        total_time+=(current_time-start)
    return total_time//n

print(solution([[10, 3], [1, 9], [1, 6]]))