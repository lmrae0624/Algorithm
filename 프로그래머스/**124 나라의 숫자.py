import math

def solution(n):
    answer = ''
    array=['4','1','2']

    answer+=array[n%3]

    while n>3:
        n=math.ceil(n/3)-1
        answer=array[n%3]+answer
        
    return answer


print(solution(16))


def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer


def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]