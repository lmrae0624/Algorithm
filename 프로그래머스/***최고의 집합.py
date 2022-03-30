def solution(n, s):
    if n>s:
        return [-1]
    
    answer = []
    a=s//n
    b=s%n
    for i in range(n):
        if b>0:
            answer.append(a+1)
            b-=1
        else:
            answer.append(a)
    answer.sort()

    return answer

print(solution(2,9))
print(solution(2,1))