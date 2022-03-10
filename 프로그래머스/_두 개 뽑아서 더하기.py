
def solution(numbers):
    from itertools import combinations 

    answer=[]  
    for a,b in combinations(numbers, 2):
        answer.append(a+b)

    return list(sorted(set(answer)))

print(solution([2,1,3,4,1]))
print(solution([0,0]))


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))