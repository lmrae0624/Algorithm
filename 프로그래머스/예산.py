def solution(d, budget):
    answer = 0
    d.sort()
    
    sum=0
    for money in d:
        sum+=money
        answer+=1
        if sum > budget:
            answer-=1
            break

    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))
print(solution([4,4,2,10],10))


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)