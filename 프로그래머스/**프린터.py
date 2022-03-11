def solution(priorities, location):
    answer = 0

    array=[0]*len(priorities)
    array[location]=1

    while priorities:
        answer+=1
        tmp=priorities.index(max(priorities))
        
        if array[tmp]==1:
            break
            
        while tmp>0:
            tmp-=1
            array.append(array.pop(0))
            priorities.append(priorities.pop(0))
        array.pop(0)
        priorities.pop(0)

    return answer

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))


def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # 첫번째 값보다 queue안에 큰게 하나라도 있으면 다시 append
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer