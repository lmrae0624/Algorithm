def solution(tickets):
    from collections import deque
    answer = []
    tickets.sort(key= lambda x: (x[0],x[1]))

    route={i:[] for i,j in tickets}
    for i,j in tickets:
        route[i].append(j)
    
    q=deque(['ICN'])
    while q :
        start=q[-1]
        if start not in route or len(route[start])==0:
            answer.append(q.pop())
        else:
            q.append(route[start].pop(0))
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))