def solution(queue1, queue2):
    from collections import deque 

    arr=queue1+queue2

    q1, q2 = deque(queue1),deque(queue2)
    total1, total2 = sum(queue1), sum(queue2)
    
    answer = 0
    while total1!=total2:
        if total1 > total2:
            tmp=q1.popleft()
            q2.append(tmp)
            total1-=tmp
            total2+=tmp
        else:
            tmp=q2.popleft()
            q1.append(tmp)
            total2-=tmp
            total1+=tmp
            
        
        answer+=1

        if list(q1)==queue2:
            return -1

    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1,1,1],[1,5]))
print(solution([1,3],[4,5]))