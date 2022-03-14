def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(arr):
    answer = 1

    for i in arr:
        answer *= i//gcd(answer,i)

    return answer

print(solution([2,6,8,14]))

from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer