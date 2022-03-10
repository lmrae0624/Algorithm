def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i]>=len(citations[:i+1]):
            answer=i+1
        
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([1,2,2,4,5]))


