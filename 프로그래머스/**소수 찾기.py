from itertools import *

def solution(numbers):
    answer = 0
    
    array=[]
    for n in numbers:
        array.append(int(n))

    for i in range(len(array)):
        tmp=list(permutations(numbers, i+1))

        for t in tmp:
            array.append(int("".join(t)))

    array=set(array)

    print(array)
  
    max_value=max(array)

    check=[True]*(max_value+1)
    check[1]=False
    check[0]=False
    
    for i in range(2,int(max_value**0.5+1)):
        if check[i]:
            j=2
            while i*j<=max_value:
                check[i*j]=False
                j+=1

    for i in array:
        if check[i]:
            answer+=1

    return answer


print(solution("17"))
print(solution("011"))


from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)