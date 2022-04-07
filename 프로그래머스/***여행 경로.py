# 도시에 한번씩들리는게 아니라 모든 항공권을 다 쓴다는게 조건

def solution(tickets):
    answer = []
    graph={i[0]:[] for i in tickets}
    for i in tickets:
        graph[i[0]].append(i[1])

    for i in graph.keys():
        graph[i].sort(reverse=True) # 뒤에서부터 pop하기 때문에 reverse한다

    stack=['ICN'] 
    while stack:
        target=stack[-1]
        print(stack)
        # 현재 공항에서 출발하는 항공권 자체가 없거나 이미 사용해서 더이상 없는 경우
        if target not in graph or len(graph[target])==0: #graph key에 target이 없거나 key에는 있는데 이미 pop해서 value가 비었을 경우
            answer.append(stack.pop())
        else:
            stack.append(graph[target].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))