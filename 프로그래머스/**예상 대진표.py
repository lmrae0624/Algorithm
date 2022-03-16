def solution(n,a,b):
    answer = 0
    
    while True:
        answer+=1
        if min(a,b)+1==max(a,b) and min(a,b)%2==1:
            break
        a=(a+1)//2
        b=(b+1)//2

    return answer

print(solution(8,4,7))
print(solution(16, 9, 12))
print(solution(8, 4, 5))

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer