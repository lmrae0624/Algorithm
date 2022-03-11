from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([1, 3, 5, 7, 9, 4, 5, 2, 1, 0]))
[9, 6, 3, 2, 1, 2, 1, 1, 1, 0]


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer